"""
# E-Mp3 Bot

###### ⓒ 2023. MaenGGo.ß STUDIO All rights reserved.
"""

if __name__ != '__main__':
    print("\n\t이 파일은 E-Mp3 봇은 메인 파일이기 때문에 다른 곳에서 불러오면 안 돼요!\n")
    from sys import exit
    exit(1)

import discord, asyncio, aiohttp, os
from discord.ext import commands
import logging
import config
import lavalink
import time
from lib import playlist

print('waiting lavalink be started')
DIR = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))
os.system("start lavalink.bat")
time.sleep(5)

# <<--- Auto Logger --->>
auto_logger = logging.getLogger()
auto_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s / [{}%(levelname)s{}] [%(name)s]: %(message)s'.format("\033[32m", "\033[0m"), datefmt='%H시 %M분 %S초')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
auto_logger.addHandler(stream_handler)
global Lava
# <<--- Class --->>
class Bot(commands.AutoShardedBot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.voice_states = True
        super().__init__(
            intents=intents,
            shard_count=config.SHARD_COUNT,
            description=config.DESCRIPTION,
            command_prefix = config.PREFIX
        )

    async def setup_hook(self):
        """- 봇이 구동되면 처음 한번 실행되는 부분"""
        self.session = aiohttp.ClientSession()

        for _dir in ['cogs']:
            cog_list = [i.split(".")[0] for i in os.listdir(_dir) if ".py" in i]
            if "__init__" in cog_list:
                cog_list.remove("__init__")
            for i in cog_list:
                print(f"{_dir.replace('/', '.')}.{i} 로드")
                await self.load_extension(f"{_dir.replace('/', '.')}.{i}")

    async def on_ready(self):
        print('Logged on as', self.user)
        try:
            await self.tree.sync(guild=(discord.Object(id=config.DEV_GUILD)))
            print('테스트 서버와 슬래시 명령어 동기화 성공')
        except Exception as e:
            print("테스트 서버와 슬래시 명령어 동기화 실패")
            print(e)
        await activity(self=self)

    # async def on_voice_state_update(self, member, before, after):
    #     print(f"voice_state_update : {member} \n {before} \n {after}\n")

# <<--- Function --->>
async def activity(self):
    await Client.wait_until_ready()
    while not Client.is_closed(): # Client가 닫히지 않았을 때 만 작동하게 / 아니면 닫힐 때 무한 요청해서 속도제한 계속 뜸
        act = config.ACTIVITY(self)
        for i in act:
            await Client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"{i}"), status=discord.Status.idle)
            try:
                print(self.lavalink)
            except:
                print("err")
            await asyncio.sleep(5)


async def main(Token: str, Client: any):
    async with Client:
        try:
            await Client.start(token=Token)
        except Exception as e:
            print("\n", e, "\n")


global Client
Client = Bot()


# <<--- Start Client --->>

try:
    asyncio.run(main(Token=config.TOKEN, Client=Client))
    # Client.run(token=config.TOKEN)
except KeyboardInterrupt:
    print("Shutdown due to KeyboardInterrupt.")
except Exception as e:
    print(f'\n다음 에러로 봇이 실행되지 않았어요.\n-> {e}\n')



