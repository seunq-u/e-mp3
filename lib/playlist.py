"""
## utils.playlist.py  
##### This is playlist function modules

* System
* User
* Playlist
* ErrorCode

###### ⓒ 2023. MaenGGo.ß STUDIO All rights reserved.
"""

import json, os, uuid
import typing


# <<<--- system --->>>

class System:
    def sum_total() -> None:
        """- 토탈 데이터 집계"""
        pass

    def get_all_playlist_heart() -> dict:
        """
        - 모든(visibility 한정) 플리의 하트 데이터 수집\n
        Returns : 
            dict: { 
                month : [{"playlist_uuid" : heart_num}],\n
                week : [{"playlist_uuid" : heart_num}], \n
                last : [{"playlist_uuid" : heart_num}] // 전날 최고 \n
            } ->> 하트 높은 순서대로 정렬 \n
        """
        pass

    def get_all_playlist_heart_live() -> list:
        """
        - 모든(visibility 한정) 플리의 현재 하트수(today) 집계\n
        Returns:
            list [
                {"playlist_uuid" : heart_num} \n
                ...
                {"playlist_uuid" : heart_num} 
            ]
        """
        pass

    def count_all_playlist_heart() -> None:
        """
        - 모든 플리의 하트 데이터 집계
        1. week, month 집계
        2. last 에 today 대입후 초기화
        """
        pass

    class Data:
        """- 데이터 관리 함수 모음"""
        def open_data(path: str) -> dict:
            """- path에서 데이터 오픈"""
            print(path)

        def edit_data(path: str, data: any) -> None:
            """- path의 데이터 수정"""
            pass

        def create_data(path: str, name: str, data: any) -> None:
            """- path 에서 data를 가지고 있는 {name}.json 생성"""
            pass

        def check_data(path: str, name: str) -> bool:
            """- path 에 name.json 이 있는지 확인"""
            pass

        def get_playlist_heart(playlist_uuid: str) -> None:
            """- playlist_uuid 에 해당하는 플리의 하트 데이터 수집"""
            pass


# <<--- user --->>

class User:
    def add_playlist(playlist_uuid: str) -> None:
        """- 유저 데이터에 플리 추가"""
        pass

    def remove_playlist(playlist_uuid: str) -> None:
        """
        - 유저 데이터에 플리 제거
        - 데이터 백업 (최대 1주) 
        - Playlist.remove 호출
        """
        # Playlist.remove(playlist_id)
        pass

    def new(user_id: int) -> None:
        """- 유저 추가"""
        pass

    def check_heart(user_id: int) -> bool:
        """- 유저가 한디리 하트를 눌렀나 확인"""
        pass

    def remove_all(user_id: int) -> None:
        """- 유저 데이터 전체 삭제"""
        pass

# <<--- playlist --->>>

class Playlist:
    def remove(playlist_uuid: str) -> None:
        """
        - DB/playlist 에서 삭제
        - 최대 백업 1주
        - User.remove_playlist() 를 통해 자동 호출됨 *
        """
        pass

    def new_uuid() -> str:
        """- 새 UUID 생성"""
        return str(uuid.uuid4())

    def create(user_id: int, name: str, description: str, visibility: int) -> None:
        """- 플리 생성"""
        pass

    def add_heart(playlist_uuid: str) -> None:
        """- 하트 추가"""
        pass
    
    def change_visibility(playlist_uuid: str, value: int) -> None:
        """- 플리 공개여부 변경"""
        pass


    class Music:
        """- 플리 """
        def add(playlist_uuid: str, pos: int, title: str, link: str, time: str, author: str, author_link: str, thumbnail: str) -> None:
            """- 플리에 음악 추가"""
            pass

        def delete(playlist_uuid: str, pos: int, link: str) -> any:
            """- 플리에서 음악 삭제"""
            pass


class ErrorCode:
    SUCCESS = 0
    ERROR = 1
    FAIL = 2