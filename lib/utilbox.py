from discord import Interaction
import config

def isAdmin(interaction: Interaction, returnMsg: str = '❌ 이 명령어는 관리자만 사용이 가능해요.'):
    """
    - 명령어를 입력한 사람이 관리자(config.ADMINS) 인지 확인해 줍니다.
    * returnMsg : f'`{returnMsg}`'
    """
    if interaction.user.id not in config.ADMINS:
        return f'`{returnMsg}`'
    else:
        return True
