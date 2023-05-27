from discord import Interaction
import config
import uuid

def isAdmin(interaction: Interaction, returnMsg: str = '❌ 이 명령어는 관리자만 사용이 가능해요.'):
    """
    - 명령어를 입력한 사람이 관리자(config.ADMINS) 인지 확인해 줍니다.
    * returnMsg : f'`{returnMsg}`'
    """
    if interaction.user.id not in config.ADMINS:
        return f'`{returnMsg}`'
    else:
        return True

def new_uuid() -> str:
    """- 새 UUID 생성"""
    return str(uuid.uuid4())

def check_heart(user_id: int) -> bool:
    """- 유저가 한디리 하트를 눌렀나 확인"""
    pass