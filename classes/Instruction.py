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


class Instruction(FileIO):
    """DBMS 가 실행하는 함수"""

    def __init__(self) -> None:
        pass

    # 유저 명령 모음
    def create_account(data: dict):
        # 실제로 json 에 접근하는 구문들
        pass

    def delete_account(data: dict):
        pass

    def alter_nickname(data: dict):
        pass

    def add_kdbl_point(data: dict):
        pass

    def alter_terms_pp(data: dict):
        pass

    def alter_terms_tos(data: dict):
        pass

    def alter_trems_mc(data: dict):
        pass

    def add_playlist(data: dict):
        pass

    def delete_playlist(data: dict):
        pass

    def add_bookmark(data: dict):
        pass

    def delete_bookmark(data: dict):
        pass

    # 플리 명령 모음
    def __init__(self) -> None:
        pass

    def create_playlist(data: dict):
        pass

    def remove_playlist(data: dict):
        pass

    def alter_name(data: dict):
        pass

    def alter_description(data: dict):
        pass

    def alter_using_custom_cover_img(data: dict):
        pass

    def alter_cover_img(data: dict):
        pass

    def alter_visibility(data: dict):
        pass

    def add_music(data: dict):
        pass

    def remove_music(data: dict):
        pass

    def add_heart(data: dict):
        pass

    def alter_dominant_color(data: dict):
        pass

    def alter_background_type(data: dict):
        "X"
        pass


class CreateInstruction():
    """DataManager.put 의 Data 인자를 만들어 주는 클래스
    """
    # <<<--- user --->>>

    def create_account(user_id: int, nickname: str, terms: tuple[bool, bool, bool]):
        # 리턴으로 dict 형 data가 나옴
        data = {
            "Ins" : Instruction.create_account,
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
