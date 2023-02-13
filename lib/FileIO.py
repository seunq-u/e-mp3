import ujson

class FileIO():
    """파일 입출력 클래스
    """
    def __init__(self) -> None:
        pass

    def open_json(self, path: str) -> dict:
        pass

    def edit_json(self, data: dict, update_data: dict) -> None:
        data.update(update_data)
        return None

    def save_json(self, path: str, data: dict) -> bool:
        pass

    def edit_json_name(self, path: str, new_name: str) -> bool:
        pass

    def delete_json(self, path: str) -> bool:
        pass
