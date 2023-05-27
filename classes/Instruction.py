"""
## libs.FileIO.py  
It's a collection of command instruction (and creation class) used in the DataManager

### func, class and value

* UserInstruction (class)
* PlaylistInstruction (class)
* CreateInstruction (class)

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""

from classes.FileIO import FileIO
from classes.Task import StatusManager
import time, random

class Instruction():
    """DBMS 가 실행하는 함수"""

    def __init__(self) -> None:
        pass

    def remove_identifier(func):
        def wrapper(data: dict, *args):
            data.pop("Instruct")
            return func(data, *args)
        return wrapper

    # <<--- 유저 명령 모음 --->>
    @remove_identifier
    def create_account(data: dict, *args):
        if (result := FileIO.make_json(path="DB//user//", name=data.get('user_id'), data=data))[0]:
            StatusManager.set_task(
                id = data.get('Identifier'),
                status='done',
                result=True
            )
        else:
            StatusManager.set_task(
                id = data.get('Identifier'),
                status='done',
                result=False,
                comment=result[1]
            )
        return 0

    @remove_identifier
    def delete_account(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def alter_nickname(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def add_kdbl_point(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def alter_terms_pp(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def alter_terms_tos(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def alter_trems_mc(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def add_playlist(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def delete_playlist(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def add_bookmark(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def delete_bookmark(data: dict, *args, **kwargs):
        pass

    
    @remove_identifier# 플리 명령 모음
    def create_playlist(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def remove_playlist(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def alter_name(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def alter_description(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def alter_using_custom_cover_img(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def alter_cover_img(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def alter_visibility(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def add_music(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def remove_music(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def add_heart(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def alter_dominant_color(data: dict, *args, **kwargs):
        pass

    @remove_identifier
    def alter_background_type(data: dict, *args, **kwargs):
        "X"
        pass


class CreateInstruction():
    """DataManager.put 의 Data 인자를 만들어 주는 클래스
    """
    # <<<--- user --->>>

    def create_account(user_id: int, nickname: str, terms: tuple[bool, bool, bool]):
        # 리턴으로 dict 형 data가 나옴
        data = {
            "Instruct" : Instruction.create_account,
            "InstructName" : 'create_account',
            "Identifier" : user_id,
            "user_id" : user_id,
            "nickname" : nickname,
            "terms" : {
                "policy_privacy" : terms[0],
                "terms_of_service" : terms[1],
                "marketing_consent" : terms[2]
            }
        }
        return data

    def delete_account():
        pass

    def alter_nickname():
        pass

    def add_kdbl_point():
        pass

    def alter_terms_pp():
        pass

    def alter_terms_tos():
        pass

    def alter_trems_mc():
        pass

    def add_playlist():
        pass

    def delete_playlist():
        pass

    def add_bookmark():
        pass

    def delete_bookmark():
        pass

    # <<<--- playlist --->>>

    def create_playlist():
        pass

    def remove_playlist():
        pass

    def alter_name():
        pass

    def alter_description():
        pass

    def alter_using_custom_cover_img():
        pass

    def alter_cover_img():
        pass

    def alter_visibility():
        pass

    def add_music():
        pass

    def alter_muisc():
        pass

    def remove_music():
        pass

    def add_heart():
        pass
