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
import copy
import datetime

class os:
    pass

os.isfile, os.rename, os.remove = isfile, rename, remove
isfile, rename, remove = None, None, None

class FileIO():
    """파일 입출력 클래스
    """
    def _check_secure_path(path: str, func_name: str = '???') -> bool:
        path_up = path.upper()
        if path_up.startswith(('DB/', 'DB//', '''DB\\''')):
            return True
        else:
            logger.error(log=f"Wrong or Disallowed Path Error : {path}", detail=f"FileIO._check_secure_path.{func_name}")
            return False

    def _check_true_path(path: str, func_name: str = '???') -> bool:
        if not os.isfile(f'{path}'):
            logger.warn(log=f"Not Found Path : {path}", detail=f"FileIO._check_true_path.{func_name}")
            return False
        return True

    def _add_json_extension(path: str, func_name: str = '???') -> str:
        try:
            path = str(path)
            if path[-5:] != '.json':
                return (path + ('.json'))
            return path
        except Exception as e:
            logger.warn(log=f"Error : {e}", detail=f"FileIO._add_json_extension.{func_name}")

    def _task_error_comment(error: str):
        return f'[{str(datetime.datetime.now())}] {error}'

    def merge_dict(original_dict, m_dict):
        merged_dict = copy.deepcopy(original_dict)

        for key, value in m_dict.items():
            if key in merged_dict and isinstance(merged_dict[key], list):
                merged_dict[key].extend(value)

            elif key in merged_dict and isinstance(merged_dict[key], dict):
                merged_dict[key] = FileIO.merge_dict(merged_dict[key], value)

            else:
                merged_dict[key] = value

        return merged_dict

    def check_default(path: str, func_name: str = '???') -> typing.Tuple[bool, str]:
        if FileIO._check_secure_path(path=path, func_name=func_name):
            path = FileIO._add_json_extension(path=path, func_name=func_name)
            if FileIO._check_true_path(path=path, func_name=func_name):
                return (True, path)
        return (False, path)

    def check_detail(detail: str):
        if detail != '':
            detail = detail + '.'
        return detail




    def make_json(path: str, name: str, data: dict = {}, detail: str = '') -> typing.Tuple[bool, typing.Any]:
        if path.endswith(('/', '//', '''\\''')): # 제대로 path 가 제대로 된 형식인지 확인
            name = FileIO._add_json_extension(name)
            path_n = path + name

            if not FileIO._check_secure_path(path=path_n, func_name=f'{FileIO.check_detail(detail)}make_json'): # 경로가 DB 인지 확인
                return False, FileIO._task_error_comment(f'[FileIO.{FileIO.check_detail(detail)}make_json] Wrong or Disallowed Path Error')

            try:
                with open(f'{path_n}', 'wb') as f:
                    f.write(orjson.dumps(data))
                return True, True

            except Exception as e:
                logger.warn(log=f'{e}', detail=f'{FileIO.check_detail(detail)}make_json')
                return False, FileIO._task_error_comment(f'[FileIO.{FileIO.check_detail(detail)}make_json] {e}')

        else:
            logger.warn(log=f'Path Should be ended by / or // or \\', detail=f"FileIO.{FileIO.check_detail(detail)}make_json")
            return False, FileIO._task_error_comment(f'[FileIO.{FileIO.check_detail(detail)}make_json] Path Should be ended by / or // or \\')

    def read_json(path: str, detail: str = '') -> typing.Tuple[typing.Union[dict, bool], typing.Union[str, None]]:
        if not (path := FileIO.check_default(path=path, func_name=f'{FileIO.check_detail(detail)}read_json'))[0]:
            return (False, f'Not Fount File in {path}')
        try:
            path = path[1]
            with open(f'{path}', 'rb') as f:
                data = orjson.loads(f.read())
            return (data, )

        except orjson.JSONDecodeError as e:
            logger.warn(log=f'JSONDecodeError: {e}', detail=f"FileIO.{FileIO.check_detail(detail)}read_json")
            return (False, f"FileIO.{FileIO.check_detail(detail)}read_json {e}")

        except Exception as e:
            logger.warn(log=f'{e}', detail=f"FileIO.{FileIO.check_detail(detail)}read_json")
            return (False, f"FileIO.{FileIO.check_detail(detail)}read_json {e}")

    def edit_json(path: str, data: dict, detail: str = '') -> typing.Tuple[bool, typing.Any]:
        f_detail = detail + '.edit_json'
        file_data = FileIO.read_json(path=path, detail=f_detail)

        if file_data[0] is False:
            return False, FileIO._task_error_comment(file_data[1])

        try:
            save_data = FileIO.merge_dict(file_data[0], data)

        except Exception as e:
            logger.error(log=f"Error {e}", detail=f'FileIO.{FileIO.check_detail(detail)}edit_json')
            return False, FileIO._task_error_comment(f'[FileIO.{FileIO.check_detail(detail)}edit_json] {e}')

        else:
            FileIO.save_json(path=path, data=save_data, detail=f_detail)
            return True, True

    def save_json(path: str, data: dict, detail: str = '') -> bool:
        if not (path := FileIO.check_default(path=path, func_name=f'{FileIO.check_detail(detail)}save_json'))[0]:
            return False
        try:
            path = path[1]
            with open(f'{path}', 'wb') as f:
                f.write(orjson.dumps(data))
            return True
        except Exception as e:
            logger.warn(log=f'{e}', detail=f"FileIO.{FileIO.check_detail(detail)}save_json")
            return False


    def rename_json(path: str, old_name: str, new_name: str, detail: str = '') -> bool:
        if not FileIO._check_secure_path(path=path, func_name=f'{FileIO.check_detail(detail)}rename_json'):
            return False

        old_name_p = FileIO._add_json_extension(path=path+old_name, func_name=f'{FileIO.check_detail(detail)}rename_json')
        new_name_p = FileIO._add_json_extension(path=path+new_name, func_name=f'{FileIO.check_detail(detail)}rename_json')

        if not FileIO._check_true_path(path=old_name_p, func_name=f'{FileIO.check_detail(detail)}rename_json'):
            return False

        try:
            os.rename(old_name_p, new_name_p)
            return True
        except Exception as e:
            logger.error(log=f'Rename Error: {e}', detail=f'{FileIO.check_detail(detail)}.rename_json')
            return False


    def remove_json(path: str, detail: str = '') -> bool:
        if not (path := FileIO.check_default(path=path, func_name=f'{FileIO.check_detail(detail)}remove_json'))[0]:
            return False
        try:
            path = path[1]
            os.remove(path)
            return True
        except Exception as e:
            logger.warn(log=f'{e}', detail=f"FileIO.{FileIO.check_detail(detail)}remove_json")
            return False
