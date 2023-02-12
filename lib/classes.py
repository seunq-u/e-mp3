"""
## utils.playlist.py  
##### This is classes module

* Playlist

###### ⓒ 2023. MaenGGo.ß STUDIO All rights reserved.
"""
import dataclasses
import copy
import time
import typing
import ujson
import multiprocessing
from multipledispatch import dispatch
from queue import Queue


class FileIO():
    """파일 입출력 클래스
    """
    def __init__(self) -> None:
        pass

    def open_json(self, ):
        pass

    def edit_json(self, ):
        pass

    def delete_json(self, ):
        pass

class UserInstruction(FileIO):
    """DataManager 가 실행하는 유저 명령 모음
    """
    def __init__(self) -> None:
        pass

    def create_account(self, ):
        # 실제로 json 에 접근하는 구문들
        pass

    def delete_account(self, ):
        pass

    def alter_nickname(self, ):
        pass

    def add_kdbl_point(self, ):
        pass

    def alter_terms_pp(self, ):
        pass

    def alter_terms_tos(self, ):
        pass

    def alter_trems_mc(self, ):
        pass

    def add_playlist(self, ):
        pass

    def delete_playlist(self, ):
        pass

    def add_bookmark(self, ):
        pass

    def delete_bookmark(self, ):
        pass

class PlaylistInstruction(FileIO):
    """DataManager 가 실행하는 플리 명령 모음
    """
    def __init__(self) -> None:
        pass

    def create_playlist(self, ):
        pass

    def remove_playlist(self, ):
        pass

    def alter_name(self, ):
        pass

    def alter_description(self, ):
        pass

    def alter_using_custom_cover_img(self, ):
        pass

    def alter_cover_img(self, ):
        pass

    def alter_visibility(self, ):
        pass

    def add_music(self, ):
        pass

    def remove_music(self, ):
        pass

    def add_heart(self, ):
        pass


class CreateInstruction():
    """DataManager.put 의 Data 인자를 만들어 주는 클래스
    """
    def __init__(self) -> None:
        pass

    # <<<--- user --->>>

    def create_account(self, ):
        # 리턴으로 dict 형 data가 나옴
        pass

    def delete_account(self, ):
        pass

    def alter_nickname(self, ):
        pass

    def add_kdbl_point(self, ):
        pass

    def alter_terms_pp(self, ):
        pass

    def alter_terms_tos(self, ):
        pass

    def alter_trems_mc(self, ):
        pass

    def add_playlist(self, ):
        pass

    def delete_playlist(self, ):
        pass

    def add_bookmark(self, ):
        pass

    def delete_bookmark(self, ):
        pass

    # <<<--- playlist --->>>

    def create_playlist(self, ):
        pass

    def remove_playlist(self, ):
        pass

    def alter_name(self, ):
        pass

    def alter_description(self, ):
        pass

    def alter_using_custom_cover_img(self, ):
        pass

    def alter_cover_img(self, ):
        pass

    def alter_visibility(self, ):
        pass

    def add_music(self, ):
        pass

    def remove_music(self, ):
        pass

    def add_heart(self, ):
        pass

class DataManager(UserInstruction, PlaylistInstruction):
    _instance = None
    _isin = False
    def __init__(self) -> None:
        raise RuntimeError("Please Call instance() instead.")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)

            cls.__DATA = {
                "user" : {},
                "playlist" : {}
            }
            cls._isin = True
            cls.__CHECK_ID= list()
            # cls.update() # multiprocessing
        return cls._instance

    @property
    def DATA(self):
        return self.__DATA

    def _getDType(self, item):
        if type(item) == int:
            return 'user'
        elif type(item) == str:
            return 'playlist'
        else:
            return 'err'

    def isDict(self, id: typing.Union[int, str]) -> bool:
        dType = self._getDType(id)
        if self.__DATA[dType].get(id) == None:
            return False
        return True

    def put(self, id: typing.Union[int, str], data: dict):
        """입력 함수

        Args:
            id (typing.Union[int, str]): playlist uuid(str) or discord user id(int)
            data (dict): {"Instruction" : data}
        """
        dType = self._getDType(id)
        if self.isDict(id):
            print("in")
            self.__DATA[dType][id].put(data)
        else:
            self.__DATA[dType][id] = Queue()
            self.__DATA[dType][id].put(data)

    def add_checker(self, data: dict):
        """dict 에서 checker 추가"""
        return data.update({"DataManager.checker": time.time()})

    def remove_checker(self, data: dict):
        """dict 에서 checker 삭제"""
        data.pop("DataManager.checker", data)
        return data

    def get_checker(self, data: dict):
        """dict 에서 checker 얻기"""
        return data.get('DataManager.checker')

    def add_checker_in_list(self, checker_id):
        """작업이 완료되었을때 __CHECK_ID에 추가"""
        self.__CHECK_ID.append(checker_id)

    def check(self, checker_id):
        """체커에 있나 검사후 삭제"""
        result = self.__CHECK_ID.__contains__(checker_id)
        if result:
            self.__CHECK_ID.remove(checker_id)
        return result

    def update(self, id: typing.Union[int, str]):
        sleepTime = 0.1
        while self._isin:
            time.sleep(sleepTime)
            # Data 를 기반으로 멀티 프로세싱을 돌림 1~8개
            # for ~
            pass



# test code
if __name__ == '__main__':
    dt = DataManager.instance()
    dt.put(10201, {"add" : 10})
    dt.put(10201, {"dlod" : 1120})
    dt.put('abc', {"a" : 10})
    print(dt.isDict(10201))
    print(dt.DATA['user'][10201].queue)
    # print(dt._getDType(101))

"""
if 유저 가입을 요청하려면
data = CreateInstruction.create_account(필수데이터) # CreateInstruction를 통해 create_account 명령에 알맞는 dict 생성
DataManager.put(discord_user_id, data) # DataManager 가 요청을 받고 queue에 추가 후 리턴으로 체커를 알려줌 (추후 이것으로 처리여부 확인)

DataManager의 update 를 통해 자동으로 체커를 다른 변수에 저장하고, DataManager.create_account(체커가 제거된 data) (UserInstruction) 요청
    -> 반환이 True 라면 DataManager.add_checker_in_list(변수로 보관된 체커)

후에 유저에게 완료 여부를 보여주기위해 DataManager.check(체커) 를 최대 15초 동안 1초에 한번 날림

"""