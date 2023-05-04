"""
# <classes/UserManager.py>
## E-Mp3 Bot User 관리/함수 모음 클래스

* UserManager

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""

class UserManager:
    @staticmethod
    def add_playlist(playlist_uuid: str) -> None:
        """- 유저 데이터에 플리 추가"""
        pass

    @staticmethod
    def remove_playlist(playlist_uuid: str) -> None:
        """
        - 유저 데이터에 플리 제거
        - 데이터 백업 (최대 1주) 
        - Playlist.remove 호출
        """
        # Playlist.remove(playlist_id)
        pass

    @staticmethod
    def new(user_id: int) -> None:
        """- 유저 추가"""
        pass

    @staticmethod
    def check_heart(user_id: int) -> bool:
        """- 유저가 한디리 하트를 눌렀나 확인"""
        pass

    @staticmethod
    def remove_all(user_id: int) -> None:
        """- 유저 데이터 전체 삭제"""
        pass