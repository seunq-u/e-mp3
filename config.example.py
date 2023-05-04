"""
# <config.py>
## E-Mp3 Bot Config Example

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""

# <<--- Bot --->>
NAME = "BOTNAME"
ID = "BOTID"
DESCRIPTION = """BOT DESCRIPTION"""
SHARD_COUNT = 1 # 샤드 개수 (최소 1, 1000~2500 서버당 1개 추가 권장)
PREFIX = f"{NAME}/"
DEBUG = False
TOKEN = "TOKEN"

def ACTIVITY(self):
    return [
        f"🎵 {len(self.guilds)}곳에서 같이 노래 듣는중..",
        "🔍 좋은 음악 찾아 다니는중..",
        "❗ /help로 도움말을 확인할 수 있어요!"
        "📜 플리 작성중..",
    ]

# 코그 이름 (cogs/ 파일이름이 아닌 코그의 클래스 이름으로 작성+대소문자 유의)
COGS = [
    'e_mp3',
    'Music'
]
COGS.sort()


# <<--- Admin --->>
ADMINS = [
    # 봇의 관리자 ID
]
DEV_GUILD = 0 # 관리자 명령어가 표시되는 서버 ID


# <<--- Emoji --->>
class Emoji:
    okay = '<:O_:1>'
    unknown = '<:Unknown:2>'
    no = '<:X_:3>'


# <<--- Lavalink --->>
class Lavalink_DATA:
    HOST = "localhost"
    PORT = 2333
    PASSWORD = "password"
    SSL = False
    REGION = "kr"
    NAME = f"{NAME}_{ID}_BOT"
    RECONNECT_ATTEMPTS = 10
    RESUME_TIMEOUT = 300