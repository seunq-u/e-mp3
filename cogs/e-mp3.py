import datetime
import typing
import discord
from discord.ext import commands
from discord import app_commands
from typing import Literal
from lib import utilbox

import config


class e_mp3(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} loaded successfully!")

    # Admin
    @app_commands.command(name='sync', description='🍀 Sync Slash Command in <Bot Dev> guild. or <Option>')
    @app_commands.describe(option='📜 동기화 할 서버를 선택해주세요!')
    @app_commands.guilds(discord.Object(id=config.DEV_GUILD))
    async def sync(self, interaction: discord.Interaction, option: Literal['this', 'etc..', 'all'], etc: str = "*ETC에 서버 ID를 입력해 주세요!*"):
        if (iAd := utilbox.isAdmin(interaction)) is False:
            await interaction.response.send_message(content=iAd)
            return 0

        if option == 'this':
            await self.bot.tree.sync(guild=(discord.Object(id=interaction.guild_id)))
            await interaction.response.send_message(f'현재 서버({interaction.guild_id})와의 명령어 동기화에 성공했습니다.', ephemeral=False)
        if option == 'all':
            await self.bot.tree.sync()
            await interaction.response.send_message(f'모든 서버({len(self.bot.guilds)}개)와의 명령어 동기화에 성공했습니다.\n\**전 서버에 적용까지 일정시간이 걸릴 수 있습니다.*', ephemeral=False)
        if option == 'etc..':
            if etc is None:
                await interaction.response.send_message(f'옵션 etc는 etc에 길드 아이디를 입력해야 합니다.', ephemeral=False)
            else:
                try:
                    await self.bot.tree.sync(guild=(discord.Object(id=int(etc))))
                except Exception as e:
                    if isinstance(e, discord.errors.Forbidden):
                        error_comment = '```HTTPS 403 에러는 접속되지 않은(알수 없는) 서버 또는 해당 서버에 슬래시 명령어 추가 권한이 없을 때 발생합니다.```'
                    else:
                        error_comment = " "
                    await interaction.response.send_message(f'다음 에러로 `{etc}` 서버와의 명령어 동기화에 실패했습니다.\n-> ```{e}```\n{error_comment}', ephemeral=False)
                    return 0    
                await interaction.response.send_message(f'`{etc}` 서버와의 명령어 동기화에 성공했습니다.', ephemeral=False)

    @app_commands.command(description="🔁 Reload Existing Cog.")
    @app_commands.describe(extension='📜 리로드 할 Cog를 입력해 주세요!')
    @app_commands.guilds(discord.Object(id=config.DEV_GUILD))
    async def reload(self, interaction: discord.Interaction, extension: str):
        start_time = datetime.datetime.now()
        if (iAd := utilbox.isAdmin(interaction)) is False:
            return await interaction.response.send_message(content=iAd)

        try:
            if extension == "all":
                for i in (extension := list(self.bot.cogs.keys())):
                    await self.bot.reload_extension(f"cogs.{i}")
                    print(f"Reload Cogs: cogs.{i}.py")
            else:
                await self.bot.reload_extension(f"cogs.{extension}")
                print(f"Reload Cogs: cogs.{extension}.py")
        except Exception as e:
            try:
                await interaction.response.send_message(content=f'`❌ cogs.{extension}.py 를 리로드중에 에러가 발생했어요.`\n-> ```{e}```')
            except discord.errors.InteractionResponded:
                await interaction.edit_original_response(content=f'`❌ cogs.{extension}.py 를 리로드중에 에러가 발생했어요.`\n-> ```{e}```')
            except Exception as e:
                print(e)
        else:
            embed = discord.Embed(title=f'{config.Emoji.okay} Reload', description=f'{extension} successfully reloaded', color=0xff00c8).add_field( 
                    name='`⏱️ Runtime ⏱️`', 
                    value=f'```py\n{datetime.datetime.now()-start_time}```', 
                    inline=False)
            await interaction.response.send_message(embed=embed)

    @app_commands.command(description="❌ Unload Cog.")
    @app_commands.describe(extension='📜 언로드 할 Cog를 입력해 주세요!')
    @app_commands.guilds(discord.Object(id=config.DEV_GUILD))
    async def unload(self, interaction: discord.Interaction, extension: str):
        start_time = datetime.datetime.now()
        if (iAd := utilbox.isAdmin(interaction)) is False:
            return await interaction.response.send_message(content=iAd)

        try:
            await self.bot.unload_extension(f"cogs.{extension}")
            print(f"Unload Cogs: cogs.{extension}.py")
            embed = discord.Embed(title=f'{config.Emoji.okay} Unload', description=f'{extension} successfully unload', color=0xff2626).add_field( 
                    name='`⏱️ Runtime ⏱️`', 
                    value=f'```py\n{datetime.datetime.now()-start_time}```', 
                    inline=False)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(content=f'`❌ cogs.{extension}.py 를 언로드중에 에러가 발생했어요.`\n-> ```{e}```')

    @app_commands.command(description="❗ Load new Cog.")
    @app_commands.describe(extension='📜 로드 할 Cog를 입력해 주세요!')
    @app_commands.guilds(discord.Object(id=config.DEV_GUILD))
    async def load(self, interaction: discord.Interaction, extension: str):
        start_time = datetime.datetime.now()
        if (iAd := utilbox.isAdmin(interaction)) is False:
            return await interaction.response.send_message(content=iAd)

        try:
            await self.bot.load_extension(f"cogs.{extension}")
            print(f"Load Cogs: cogs.{extension}.py")
            embed = discord.Embed(title=f'{config.Emoji.okay} Load', description=f'{extension} successfully load', color=0x26ff7a).add_field( 
                    name='`⏱️ Runtime ⏱️`', 
                    value=f'```py\n{datetime.datetime.now()-start_time}```', 
                    inline=False)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(content=f'`❌ cogs.{extension}.py 를 로드중에 에러가 발생했어요.`\n-> ```{e}```')

    @app_commands.command(description="❗ Shutdown Bot")
    @app_commands.guilds(discord.Object(id=config.DEV_GUILD))
    async def shutdown(self, interaction: discord.Interaction):
        if (iAd := utilbox.isAdmin(interaction)) is False:
            return await interaction.response.send_message(content=iAd)

        print(f"SlashCommand -> ShutdownBot request is received from {interaction.user}({interaction.id})")
        await interaction.response.send_message(content=f'`✔️ SHUTDOWN`')
        nodes = self.bot.lavalink.node_manager.available_nodes
        for i in nodes:
            # await i.destroy()
            self.bot.lavalink.node_manager.remove_node(node=i)
            print(f'remove node - {i}')
        await self.bot.close()

    @app_commands.command(description="📄 Get lavaink nodes and players info.")
    @app_commands.guilds(discord.Object(id=config.DEV_GUILD))
    async def getnode(self, interaction: discord.Interaction):
        if (iAd := utilbox.isAdmin(interaction)) is False:
            return await interaction.response.send_message(content=iAd)

        await interaction.response.send_message("`❗ 라바링크 노드(lavalink node)의 정보를 얻고 있어요..`")
        nodes = self.bot.lavalink.node_manager.available_nodes
        if len(nodes) == 0:
            await interaction.edit_original_response(content = f'`❌ 노드가 없어요.. - {nodes}`')
        else:
            Text = ''
            for i in range(len(nodes)):
                players = nodes[i].players
                IsPlaying = list()
                IsntPlaying = list()
                for p in players:
                    if p.is_playing is True:
                        IsPlaying.append(p)
                    else:
                        IsntPlaying.append(p)
                
                Text = Text + '\n' + f'[34m{i+1}. [37m{nodes[i]} [1m->\n\t\tIs Playing [0m [34m{IsPlaying}[30m([35m{len(IsPlaying)}[30m)[0m\n\t\t[37m[1mIsn\'t Playing [0m [34m{IsntPlaying}[30m([35m{len(IsntPlaying)}[30m)[0m'
            Text = '```ansi' + Text + '```'
            await interaction.edit_original_response(content = f'`✔️ {len(nodes)}개의 노드를 찾았어요!`\n{Text}')



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(e_mp3(bot=bot))
