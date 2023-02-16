import typing
import discord
from discord.ext import commands
from discord import app_commands
import lavalink
import re
# from lavalink.filters import Karaoke, Timescale, Tremolo, Vibrato, Rotation, LowPass, ChannelMix, Volume
import config
url_rx = re.compile(r'https?://(?:www\.)?.+')

async def command_before_invoke(self, interaction: discord.Interaction) -> bool: # 명령어가 실행되기 전 실행되야 하는 명령어
    """- Command before-invoke handler. (핸들러를 호출하기전 실행하는 명령어)"""
    # DM 이 아닌지 확인
    guild_check = interaction.guild is not None
    # print(dir(ctx.user.voice.channel), ctx.user.voice.channel)
    #  This is essentially the same as `@commands.guild_only()`
    #  except it saves us repeating ourselves (and also a few lines).
    # 응답 지연 -> 보낼려면 await interaction.followup.send() 를 사용
    await interaction.response.defer()

    if guild_check:
        ensure = await ensure_voice(self, interaction) # ensure_voice 호출
        #  유저가 봇과 같은 채널에 있는지 확인해줌

    return ensure


async def ensure_voice(self, interaction: discord.Interaction) -> bool: # 에러 방지
    """ 봇의 권한과, 유저가 봇과 같은 음성채널에 있는지 확인 하는 함수"""
    player = self.bot.lavalink.player_manager.create(interaction.guild.id) #, endpoint=str(ctx.guild.region))
    should_connect = interaction.command.name in ('재생', '연결', ) # 자동 연결 + 연결해야 해야 작동하는 명령어
    free_commands = interaction.command.name in ( '도움말', ) # 연결 여부없이 작동하는 명령어

    if free_commands is True:
        return True

    # 음성채널에 유저가 존재하는지 확인
    if not interaction.user.voice or not interaction.user.voice.channel:
        await interaction.followup.send("`❗ 먼저 음성채널에 들어가야 이 명령어를 사용할 수 있어요!`", ephemeral=True)
        return False

    # 음성채널과 봇(재생 player)이 연결안된 경우
    if not player.is_connected:
        if not should_connect: # should connect가 아닐경우
            await interaction.followup.send("`❗ 연결된 채널이 없어요..`", ephemeral=True)
            return False

        player.store('text_channel_id', interaction.channel.id)
        try:
            await interaction.user.voice.channel.connect(cls=LavalinkVoiceClient, self_deaf=True)
        except Exception as e:
            try:
                await interaction.guild.voice_client.disconnect(force=True)
                await interaction.user.voice.channel.connect(cls=LavalinkVoiceClient, self_deaf=True)
            except Exception as e:
                print(e)
                await interaction.followup.send("`❗ 연결중에 에러가 발생했어요..`")
                return False

    # 음성채널과 봇이 연결된 경우
    else:
        if int(player.channel_id) != interaction.user.voice.channel.id:
            await interaction.followup.send("`❗ 제가 연결된 음성 채널에서 명령어를 사용해주세요!`", ephemeral=True)
            return False

    return True

class LavalinkVoiceClient(discord.VoiceClient):
    def __init__(self, client: discord.Client, channel: discord.abc.Connectable):
        self.client = client
        self.channel = channel

        # self.client 에 lavalink 가 이미 있는지 확인
        if hasattr(self.client, 'lavalink'):
            self.lavalink = self.client.lavalink
        else:
            self.client.lavalink = lavalink.Client(client.user.id)
            self.client.lavalink.add_node(
                host = config.Lavalink_DATA.HOST,
                port = config.Lavalink_DATA.PORT,
                password = config.Lavalink_DATA.PASSWORD,
                region = config.Lavalink_DATA.REGION,
                name = config.Lavalink_DATA.NAME,
                reconnect_attempts = config.Lavalink_DATA.RECONNECT_ATTEMPTS,
                resume_timeout = config.Lavalink_DATA.RESUME_TIMEOUT
            )
            self.lavalink = self.client.lavalink

    async def on_voice_server_update(self, data):
        """- voice_update_handler"""
        lavalink_data = {
            't': 'VOICE_SERVER_UPDATE',
            'd': data
        }
        await self.lavalink.voice_update_handler(lavalink_data)

    async def on_voice_state_update(self, data):
        """- voice_update_handler"""
        lavalink_data = {
                't': 'VOICE_STATE_UPDATE',
                'd': data
                }
        await self.lavalink.voice_update_handler(lavalink_data)

    async def connect(self, *, timeout: float, reconnect: bool, self_deaf: bool = True, self_mute: bool = False) -> None:
        """
        봇을 음성 채널에 연결하고 player_manager가 아직 없는 경우 player_manager를 만듬
        """
        # 새로운 voice client 생성시 player_manager가 존재하는지 확인
        await self.channel.guild.change_voice_state(channel=self.channel, self_mute=self_mute, self_deaf=self_deaf)

    async def disconnect(self, *, force: bool = False) -> None:
        """
        연결끊기 후 실행중인 플레이어를 정리하고 클라이언트를 종료
        """
        player = self.lavalink.player_manager.get(self.channel.guild.id)

        # 연결 안돼 있으면 return
        if not force and not player.is_connected:
            return

        # 연결 끊기 (None 이 끊김을 의미함)
        await self.channel.guild.change_voice_state(channel=None)

        # update the channel_id of the player to None
        # this must be done because the on_voice_state_update that would set channel_id
        # to None doesn't get dispatched after the disconnect
        player.channel_id = None
        await player.reset_equalizer()
        self.cleanup()

class Music(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

        if not hasattr(bot, 'lavalink'):  # This ensures the client isn't overwritten during cog reloads.
            bot.lavalink = lavalink.Client(bot.user.id)
            bot.lavalink.add_node(
                host = config.Lavalink_DATA.HOST,
                port = config.Lavalink_DATA.PORT,
                password = config.Lavalink_DATA.PASSWORD,
                region = config.Lavalink_DATA.REGION,
                name = config.Lavalink_DATA.NAME,
                reconnect_attempts = config.Lavalink_DATA.RECONNECT_ATTEMPTS,
                resume_timeout = config.Lavalink_DATA.RESUME_TIMEOUT
            )

        lavalink.add_event_hook(self.track_hook)

        # @self.bot.event
        # async def on_voice_state_update(member, before, after):
        #     print(f"voice_state_update : {member} \n {before} \n {after}\n")
        #     try:
        #         print(after.channel.members)
        #     except:
        #         print(before.channel.members)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        print(f"voice_state_update : {member} \n {before} \n {after}\n")
        try:
            print(after.channel.members)
        except:
            print(before.channel.members)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} loaded successfully!")

    def cog_unload(self):
        """- 코그 언로드 핸들러. 코그가 언로드 되면 모든 이벤트 후크 제거."""
        self.bot.lavalink._event_hooks.clear()

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.response.send_message(error.original)

    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            # When this track_hook receives a "QueueEndEvent" from lavalink.py
            # it indicates that there are no tracks left in the player's queue.
            # To save on resources, we can tell the bot to disconnect from the voicechannel.
            guild_id = event.player.guild_id
            guild = self.bot.get_guild(guild_id)
            await guild.voice_client.disconnect(force=True)



    @app_commands.command(name="재생", description="🎵 음악을 재생해요!", nsfw=False)
    @app_commands.describe(query='📜 음악 이름을 입력해 주세요!')
    @app_commands.guilds(discord.Object(id=config.DEV_GUILD))
    async def play(self, interaction: discord.Interaction, query: str):
        """ Searches and plays a song from a given query. """
        if not await command_before_invoke(self=self, interaction=interaction):
            return None

        # 캐시로부터 재생 플레이어 얻기
        player = self.bot.lavalink.player_manager.get(interaction.guild.id)
        # < > 제거 (디스코드에서 URL 임베딩 제한용으로 쓰임)
        query = query.strip('<>')

        # URL 이 유튜브 링크인지 확인하고 접두사 추가 / URL 이 아니면 일반 검색
        # SoundCloud 는 "scsearch:" 로
        if not url_rx.match(query):
            query = f'ytsearch:{query}'

        # lavalink 요청
        results = await player.node.get_tracks(query)

        # Results could be None if Lavalink returns an invalid response (non-JSON/non-200 (OK)).
        # Alternatively, results.tracks could be an empty array if the query yielded no tracks.
        if not results or not results.tracks:
            return await interaction.followup.send(content='`❗ 검색 결과가 없어요!`')

        embed = discord.Embed(color=discord.Color.blurple())

        # 로드타입:
        #   TRACK_LOADED    - single video/direct URL
        #   PLAYLIST_LOADED - direct URL to playlist
        #   SEARCH_RESULT   - query prefixed with either ytsearch: or scsearch:.
        #   NO_MATCHES      - query yielded no results
        #   LOAD_FAILED     - most likely, the video encountered an exception during loading.
        if results.load_type == 'PLAYLIST_LOADED':
            tracks = results.tracks

            for track in tracks:
                # Add all of the tracks from the playlist to the queue.
                player.add(requester=interaction.user.id, track=track)

            embed.title = 'Playlist Enqueued!'
            embed.description = f'{results.playlist_info.name} - {len(tracks)} tracks'
        else:
            track = results.tracks[0]
            embed.title = 'Track Enqueued'
            embed.description = f'[{track.title}]({track.uri})'

            player.add(requester=interaction.user.id, track=track)


        await interaction.followup.send(embed=embed)


        # 재생중이지 않는다면 재생 시작
        if not player.is_playing:
            await player.play()

    @app_commands.command(name="연결", description="🎤 음성 채널에 연결해요!")
    @app_commands.guilds(discord.Object(id=config.DEV_GUILD))
    async def 연결(self, interaction: discord.Interaction):
        if not await command_before_invoke(self=self, interaction=interaction):
            return None

        # player = self.bot.lavalink.player_manager.get(interaction.guild.id)
        await interaction.followup.send(f'<#{interaction.user.voice.channel.id}>에 연결했어요!')

    @app_commands.command(name="연결끊기", description="❗ 음성 채널에서 나가요!")
    @app_commands.guilds(discord.Object(id=config.DEV_GUILD))
    async def 연결끊기(self, interaction: discord.Interaction):
        if not await command_before_invoke(self=self, interaction=interaction):
            return None

        player = self.bot.lavalink.player_manager.get(interaction.guild.id)

        if not player.is_connected:
            # We can't disconnect, if we're not connected.
            return await interaction.followup.send(content="`❗ 연결된 채널이 없어요..`", ephemeral=True)
        # print(player.channel_id, interaction.user.voice.channel.id)
        if not interaction.user.voice or (player.is_connected and interaction.user.voice.channel.id != int(player.channel_id)):
            # Abuse prevention. Users not in voice channels, or not in the same voice channel as the bot
            # may not disconnect the bot.
            return await interaction.followup.send(content="`❗ 제가 연결된 음성 채널에서 명령어를 사용해주세요!`", ephemeral=True)

        # Disconnectiong
        # Clear the queue to ensure old tracks don't start playing
        # when someone else queues something.
        player.queue.clear()
        # Stop the current track so Lavalink consumes less resources.
        await player.stop()
        # Disconnect from the voice channel.
        try:
            await interaction.guild.voice_client.disconnect(force=True) # 또는 await interaction.voice_client.disconnect(force=True)
        except AttributeError as e:
            print(e)
        finally:
            player.channel_id = None
            await interaction.followup.send('`음성채널을 나갔어요!`')

        # print(f"<{interaction.user.voice.channel} | {interaction.user.voice.channel.id}> 연결 해제")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Music(bot=bot))
