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
    def __init__(self) -> None:
        pass


    # 유저 명령 모음
    def create_account(self, data: dict):
        # 실제로 json 에 접근하는 구문들
        pass

    def delete_account(self, data: dict):
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

    # 플리 명령 모음
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

    def alter_dominant_color(self, ):
        pass

    def alter_background_type(self, ):
        "X"
        pass


class CreateInstruction():
    """DataManager.put 의 Data 인자를 만들어 주는 클래스
    """
    def __init__(self) -> None:
        pass

    # <<<--- user --->>>

    def create_account(self, user_id: int, nickname: str, terms: tuple[bool, bool, bool]):
        # 리턴으로 dict 형 data가 나옴
        data = {
            "user_id" : user_id,
            "nickname" : nickname,
            "terms" : {
                "policy_privacy" : terms[0],
                "terms_of_service" : terms[1],
                "marketing_consent" : terms[2]
            }
        }
        return data

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

    def alter_muisc(self, ):
        pass

    def remove_music(self, ):
        pass

    def add_heart(self, ):
        pass
