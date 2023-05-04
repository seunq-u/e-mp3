"""
# <classes/playlistManager.py>
## E-Mp3 Bot Playlist 관리/함수 모음 클래스

* PlaylistManager

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""

import typing
import uuid


class PlaylistManager:
    @staticmethod
    def remove(playlist_uuid: str) -> None:
        """
        - DB/playlist 에서 삭제
        - 최대 백업 1주
        - User.remove_playlist() 를 통해 자동 호출됨 *
        """
        pass

    @staticmethod
    def new_uuid() -> str:
        """- 새 UUID 생성"""
        return str(uuid.uuid4())

    @staticmethod
    def create(user_id: int, name: str, description: str, visibility: int) -> None:
        """- 플리 생성"""
        pass

    @staticmethod
    def add_heart(playlist_uuid: str) -> None:
        """- 하트 추가"""
        pass

    @staticmethod
    def change_visibility(playlist_uuid: str, value: int) -> None:
        """- 플리 공개여부 변경"""
        pass


    class Music:
        """- 음악관리 """

        @staticmethod
        def add(playlist_uuid: str, pos: int, title: str, link: str, time: str, author: str, author_link: str, thumbnail: str) -> None:
            """- 플리에 음악 추가"""
            pass

        @staticmethod
        def delete(playlist_uuid: str, pos: int, link: str) -> any:
            """- 플리에서 음악 삭제"""
            pass
