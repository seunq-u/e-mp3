"""
## libs.FileIO.py  
Directly access and manipulate of json file(user data, player data, etc. )

### func, class and value

* FileIO (class)

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""

import typing
import orjson
from os.path import isfile
from os import rename, remove
from libs import logger
from pydantic.utils import deep_update

class os:
    pass

os.isfile, os.rename, os.remove = isfile, rename, remove
rename, isfile, remove = None, None, None
# class FileIOError():
#     class WrongORDisallowedPath(Exception):
#         def __str__(self):
#             return "Wrong or Disallowed Path Error"

class FileIO():
    """파일 입출력 클래스
    """
    def __init__(self) -> None:
        pass

    def _check_secure_path(self, path: str, func_name: str = '???') -> bool:
        path_up = path.upper()
        if path_up.startswith(('DB/', 'DB//', '''DB\\''')):
            return True
        else:
            logger.error(log=f"Wrong or Disallowed Path Error : {path}", detail=f"FileIO._check_secure_path.{func_name}")
            return False

    def _check_true_path(self, path: str, func_name: str = '???') -> bool:
        if not os.isfile(f'{path}'):
            logger.warn(log=f"Not Found Path : {path}", detail=f"FileIO._check_true_path.{func_name}")
            return False
        return True

    def _add_json_extension(self, path: str, func_name: str = '???') -> str:
        try:
            path = str(path)
            if path[-5:] != '.json':
                return (path + ('.json'))
            return path
        except Exception as e:
            logger.warn(log=f"Error : {e}", detail=f"FileIO._add_json_extension.{func_name}")


    def check_default(self, path: str, func_name: str = '???') -> tuple[bool, str]:
        if self._check_secure_path(path=path, func_name=func_name):
            path = self._add_json_extension(path=path, func_name=func_name)
            if self._check_true_path(path=path, func_name=func_name):
                return (True, path)
        return (False, path)

    def check_detail(self, detail: str):
        if detail != '':
            detail = detail + '.'
        return detail




    def make_json(self, path: str, name: str, data: dict = {}, detail: str = '') -> bool:
        if path.endswith(('/', '//', '''\\''')): # 제대로 path 가 제대로 된 형식인지 확인
            name = self._add_json_extension(name)
            path_n = path + name

            if not self._check_secure_path(path=path_n, func_name=f'{self.check_detail(detail)}make_json'): # 경로가 DB 인지 확인
                return False

            try:
                with open(f'{path_n}', 'wb') as f:
                    f.write(orjson.dumps(data))
                return True

            except Exception as e:
                logger.warn(log=f'{e}', detail=f'{self.check_detail(detail)}make_json')
                return False

        else:
            logger.warn(log=f'Path Should be ended by / or // or \\', detail=f"FileIO.{self.check_detail(detail)}make_json")

    def read_json(self, path: str, detail: str = '') -> typing.Union[dict, bool]:
        if not (path := self.check_default(path=path, func_name=f'{self.check_detail(detail)}read_json'))[0]:
            return False
        try:
            path = path[1]
            with open(f'{path}', 'rb') as f:
                data = orjson.loads(f.read())
            return data
        except orjson.JSONDecodeError as e:
            logger.warn(log=f'JSONDecodeError: {e}', detail=f"FileIO.{self.check_detail(detail)}read_json")
            return dict()
        except Exception as e:
            logger.warn(log=f'{e}', detail=f"FileIO.{self.check_detail(detail)}read_json")
            return False

    def edit_json(self, path: str, update_data: dict, detail: str = '') -> bool:
        f_detail = detail + '.edit_json'
        file_data = self.read_json(path=path, detail=f_detail)
        if file_data is False:
            return False
        try:
            save_data = deep_update(file_data, update_data)
        except Exception as e:
            logger.error(log=f"Error {e}", detail=f'FileIO.{self.check_detail(detail)}edit_json')
            return False
        else:
            self.save_json(path=path, data=save_data, detail=f_detail)

    def save_json(self, path: str, data: dict, detail: str = '') -> bool:
        if not (path := self.check_default(path=path, func_name=f'{self.check_detail(detail)}save_json'))[0]:
            return False
        try:
            path = path[1]
            with open(f'{path}', 'wb') as f:
                f.write(orjson.dumps(data))
            return True
        except Exception as e:
            logger.warn(log=f'{e}', detail=f"FileIO.{self.check_detail(detail)}save_json")
            return False


    def rename_json(self, path: str, old_name: str, new_name: str, detail: str = '') -> bool:
        if not self._check_secure_path(path=path, func_name=f'{self.check_detail(detail)}rename_json'):
            return False

        old_name_p = self._add_json_extension(path=path+old_name, func_name=f'{self.check_detail(detail)}rename_json')
        new_name_p = self._add_json_extension(path=path+new_name, func_name=f'{self.check_detail(detail)}rename_json')

        if not self._check_true_path(path=old_name_p, func_name=f'{self.check_detail(detail)}rename_json'):
            return False

        try:
            os.rename(old_name_p, new_name_p)
            return True
        except Exception as e:
            logger.error(log=f'Rename Error: {e}', detail=f'{self.check_detail(detail)}.rename_json')
            return False


    def remove_json(self, path: str, detail: str = '') -> bool:
        if not (path := self.check_default(path=path, func_name=f'{self.check_detail(detail)}remove_json'))[0]:
            return False
        try:
            path = path[1]
            os.remove(path)
            return True
        except Exception as e:
            logger.warn(log=f'{e}', detail=f"FileIO.{self.check_detail(detail)}remove_json")
            return False
