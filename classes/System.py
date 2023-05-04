"""
# <classes/System.py>
## E-Mp3 Bot System 관리/함수 모음 클래스

* System

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""


class System:
    @staticmethod
    def sum_total() -> None:
        """- 토탈 데이터 집계"""
        pass

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def count_all_playlist_heart() -> None:
        """
        - 모든 플리의 하트 데이터 집계
        1. week, month 집계
        2. last 에 today 대입후 초기화
        """
        pass

    class Data:
        """- 데이터 관리 함수 모음"""

        @staticmethod
        def open_data(path: str) -> dict:
            """- path에서 데이터 오픈"""
            print(path)

        @staticmethod
        def edit_data(path: str, data: any) -> None:
            """- path의 데이터 수정"""
            pass

        @staticmethod
        def create_data(path: str, name: str, data: any) -> None:
            """- path 에서 data를 가지고 있는 {name}.json 생성"""
            pass

        @staticmethod
        def check_data(path: str, name: str) -> bool:
            """- path 에 name.json 이 있는지 확인"""
            pass

        @staticmethod
        def get_playlist_heart(playlist_uuid: str) -> None:
            """- playlist_uuid 에 해당하는 플리의 하트 데이터 수집"""
            pass