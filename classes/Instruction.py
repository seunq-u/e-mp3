"""
## libs.Instruction.py  
It's a collection of command instruction (and creation class) used in the DBMS

### func, class and value

* Instruction (class)
* CreateInstruction (class)

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""

from classes.FileIO import FileIO
from classes.Task import StatusManager


class Instruction():
    """DBMS 가 실행하는 함수"""

    def __init__(self) -> None:
        pass

    def remove_identifier(func):
        def wrapper(data: dict, *args):
            data.pop("Instruct")
            return func(data, *args)
        return wrapper

    # 자주 사용되는 함수
    def alter_user(data: dict, *args):
        print(data)
        if (result := FileIO.edit_json(path=f"DB//user//{data.get('Identifier')}.json", data=data))[0]:
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
        return True

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
        return True

    @remove_identifier
    def delete_account(data: dict, *args):
        pass

    @remove_identifier
    def alter_nickname(data: dict, *args):
        return Instruction.alter_user(data=data)

    @remove_identifier
    def add_kdbl_point(data: dict, *args):
        pass

    @remove_identifier
    def alter_terms_pp(data: dict, *args):
        return Instruction.alter_user(data=data)

    @remove_identifier
    def alter_terms_tos(data: dict, *args):
        return Instruction.alter_user(data=data)

    @remove_identifier
    def alter_trems_mc(data: dict, *args):
        return Instruction.alter_user(data=data)

    @remove_identifier
    def add_playlist(data: dict, *args):
        return Instruction.alter_user(data=data)

    @remove_identifier
    def delete_playlist(data: dict, *args):
        pass

    @remove_identifier
    def add_bookmark(data: dict, *args):
        return Instruction.alter_user(data=data)

    @remove_identifier
    def delete_bookmark(data: dict, *args):
        pass


    # 플리 명령 모음
    @remove_identifier
    def create_playlist(data: dict, *args):
        pass

    @remove_identifier
    def remove_playlist(data: dict, *args):
        pass

    @remove_identifier
    def alter_name(data: dict, *args):
        pass

    @remove_identifier
    def alter_description(data: dict, *args):
        pass

    @remove_identifier
    def alter_using_custom_cover_img(data: dict, *args):
        pass

    @remove_identifier
    def alter_cover_img(data: dict, *args):
        pass

    @remove_identifier
    def alter_visibility(data: dict, *args):
        pass

    @remove_identifier
    def add_music(data: dict, *args):
        pass

    @remove_identifier
    def remove_music(data: dict, *args):
        pass

    @remove_identifier
    def add_heart(data: dict, *args):
        pass

    @remove_identifier
    def alter_dominant_color(data: dict, *args):
        pass

    @remove_identifier
    def alter_background_type(data: dict, *args):
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
            },
            "playlist" : [ ],
            "bookmark" : [ ]
        }
        return data

    def delete_account():
        pass

    def alter_nickname(user_id: int, nickname: str):
        data = {
            "Instruct" : Instruction.alter_nickname,
            "InstructName" : 'alter_nickname',
            "Identifier" : user_id,
            "nickname" : nickname
        }
        return data

    def add_kdbl_point():
        pass

    def alter_terms_pp(user_id: int, term_pp: bool):
        data = {
            "Instruct" : Instruction.alter_terms_pp,
            "InstructName" : 'alter_terms_pp',
            "Identifier" : user_id,
            "terms" : {
                "policy_privacy" : term_pp,
            }
        }
        return data

    def alter_terms_tos(user_id: int, term_tos: bool):
        data = {
            "Instruct" : Instruction.alter_terms_tos,
            "InstructName" : 'alter_terms_tos',
            "Identifier" : user_id,
            "terms" : {
                "terms_of_service" : term_tos,
            }
        }
        return data

    def alter_trems_mc(user_id: int, term_mc: bool):
        data = {
            "Instruct" : Instruction.alter_trems_mc,
            "InstructName" : 'alter_trems_mc',
            "Identifier" : user_id,
            "terms" : {
                "marketing_consent" : term_mc
            }
        }
        return data

    def add_playlist(user_id: int, playlist_uuid: str):
        data = {
            "Instruct" : Instruction.add_playlist,
            "InstructName" : 'add_playlist',
            "Identifier" : user_id,
            "playlist" : [playlist_uuid]
        }
        return data

    def delete_playlist():
        pass

    def add_bookmark(user_id: int, playlist_uuid: str):
        data = {
            "Instruct" : Instruction.add_bookmark,
            "InstructName" : 'add_bookmark',
            "Identifier" : user_id,
            "bookmark" : [playlist_uuid]
        }
        return data

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
