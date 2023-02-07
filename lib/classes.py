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
from multipledispatch import dispatch
from queue import Queue

@dataclasses.dataclass
class playlist():
    pass

class DataManager(object):
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
                "user" : {
                    
                },
                "playlist" : {
                    
                }
            }
            cls._isin = True
            # cls.update() # 쓰레드로
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
        dType = self._getDType(id)
        if self.isDict(id):
            print("in")
            self.__DATA[dType][id].put(data)
        else:
            self.__DATA[dType][id] = Queue()
            self.__DATA[dType][id].put(data)

    def update(self, id: typing.Union[int, str]):
        sleepTime = 0.1
        while self._isin:
            time.sleep(sleepTime)
            pass


if __name__ == '__main__':
    dt = DataManager.instance()
    dt.put(10201, {"add" : 10})
    dt.put(10201, {"dlod" : 1120})
    dt.put('abc', {"a" : 10})
    print(dt.isDict(10201))
    print(dt.DATA['user'][10201].queue)
    # print(dt._getDType(101))
