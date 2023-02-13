from lib.classes.FileIO import FileIO


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
