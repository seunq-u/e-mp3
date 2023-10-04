"""
## classes.Instruction.py  
It's a collection of command instruction (and creation class) used in the DBMS

### func, class and value

* Instruction (class)
* CreateInstruction (class)

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""

import time
import typing
from classes.FileIO import FileIO
from classes.Task import StatusManager


class Instruction():
    """DBMS 가 실행하는 함수"""

    def __init__(self) -> None:
        pass

    def get_path_from_identifier(id: str) -> str:
        return id.split('?t=')[0]

    def rmv_fnc_in_dict(func):
        # CreateInstruct의 함수 객체를 삭제
        def wrapper(data: dict, *args):
            data.pop("Instruct")
            return func(data, *args)
        return wrapper

    # 자주 사용되는 함수
    def alter_user(data: dict, *args):
        id_removed_time = Instruction.get_path_from_identifier(id = data.get('Identifier'))
        if (result := FileIO.edit_json(path=f"DB//user//{id_removed_time}.json", data=data))[0]:
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
    @rmv_fnc_in_dict
    def create_account(data: dict, *args):
        id_removed_time = Instruction.get_path_from_identifier(id = data.get('Identifier'))
        if (result := FileIO.make_json(path="DB//user//", name=id_removed_time, data=data))[0]:
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

    @rmv_fnc_in_dict
    def delete_account(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def alter_nickname(data: dict, *args):
        return Instruction.alter_user(data=data)

    @rmv_fnc_in_dict
    def add_kdbl_point(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def alter_terms_pp(data: dict, *args):
        return Instruction.alter_user(data=data)

    @rmv_fnc_in_dict
    def alter_terms_tos(data: dict, *args):
        return Instruction.alter_user(data=data)

    @rmv_fnc_in_dict
    def alter_trems_mc(data: dict, *args):
        return Instruction.alter_user(data=data)

    @rmv_fnc_in_dict
    def add_playlist(data: dict, *args):
        return Instruction.alter_user(data=data)

    @rmv_fnc_in_dict
    def delete_playlist(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def add_bookmark(data: dict, *args):
        return Instruction.alter_user(data=data)

    @rmv_fnc_in_dict
    def delete_bookmark(data: dict, *args):
        pass


    # 플리 명령 모음
    @rmv_fnc_in_dict
    def create_playlist(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def remove_playlist(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def alter_name(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def alter_description(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def alter_using_custom_cover_img(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def alter_cover_img(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def alter_visibility(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def add_music(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def remove_music(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def add_heart(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def alter_dominant_color(data: dict, *args):
        pass

    @rmv_fnc_in_dict
    def alter_background_type(data: dict, *args):
        "X"
        pass


class CreateInstruction():
    """DataManager.put 의 Data 인자를 만들어 주는 클래스
    """
    # <<<--- user --->>>

    def crt_inst_idn(id: typing.Union[str, int]) -> str:
        # 명령어 식별자 생성
        return f'{id}?t={time.time()}'

    def crt_df_dict(instruct: Instruction, instruct_name: str, id: typing.Union[str, int]) -> dict:
        return {
            "Instruct" : instruct,
            "InstructName" : instruct_name,
            "Identifier" : CreateInstruction.crt_inst_idn(id)
            }

    def create_account(user_id: int, nickname: str, terms: typing.Tuple[bool, bool, bool]) -> dict:
        # 리턴으로 dict 형 data가 나옴
        data : dict = CreateInstruction.crt_df_dict(Instruction.create_account, 'create_account', user_id)
        data.update({
            "user_id" : user_id,
            "nickname" : nickname,
            "terms" : {
                "policy_privacy" : terms[0],
                "terms_of_service" : terms[1],
                "marketing_consent" : terms[2]
            },
            "playlist" : [ ],
            "bookmark" : [ ]
        })
        return data

    def delete_account() -> dict:
        pass

    def alter_nickname(user_id: int, nickname: str) -> dict:
        data : dict = CreateInstruction.crt_df_dict(Instruction.alter_nickname, 'alter_nickname', user_id)
        data.update({"nickname" : nickname})
        return data

    def add_kdbl_point() -> dict:
        pass

    def alter_terms_pp(user_id: int, term_pp: bool) -> dict:
        data : dict = CreateInstruction.crt_df_dict(Instruction.alter_terms_pp, 'alter_terms_pp', user_id)
        data.update({
            "terms" : {
                "policy_privacy" : term_pp,
            }
        })
        return data

    def alter_terms_tos(user_id: int, term_tos: bool) -> dict:
        data : dict = CreateInstruction.crt_df_dict(Instruction.alter_terms_tos, 'alter_terms_tos', user_id)
        data.update({
            "terms" : {
                "terms_of_service" : term_tos,
            }
        })
        return data

    def alter_trems_mc(user_id: int, term_mc: bool) -> dict:
        data : dict = CreateInstruction.crt_df_dict(Instruction.alter_trems_mc, 'alter_trems_mc', user_id)
        data.update({
            "terms" : {
                "marketing_consent" : term_mc
            }
        })
        return data

    def add_playlist(user_id: int, playlist_uuid: str) -> dict:
        data : dict = CreateInstruction.crt_df_dict(Instruction.add_playlist, 'add_playlist', user_id)
        data.update({"playlist" : [playlist_uuid]})
        return data

    def delete_playlist() -> dict:
        pass

    def add_bookmark(user_id: int, playlist_uuid: str) -> dict:
        data : dict = CreateInstruction.crt_df_dict(Instruction.add_bookmark, 'add_bookmark', user_id)
        data.update({"bookmark" : [playlist_uuid]})

        return data

    def delete_bookmark() -> dict:
        pass

    # <<<--- playlist --->>>

    def create_playlist() -> dict:
        pass

    def remove_playlist() -> dict:
        pass

    def alter_name() -> dict:
        pass

    def alter_description() -> dict:
        pass

    def alter_using_custom_cover_img() -> dict:
        pass

    def alter_cover_img() -> dict:
        pass

    def alter_visibility() -> dict:
        pass

    def add_music() -> dict:
        pass

    def alter_muisc() -> dict:
        pass

    def remove_music() -> dict:
        pass

    def add_heart() -> dict:
        pass
