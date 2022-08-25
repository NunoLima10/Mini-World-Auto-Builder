from src.file_status import FileStatus

import pathlib

class FileData:
    def __init__(self, path: pathlib.Path) -> None:
        self.file_path = path
        self.full_name = self.file_path.name

        self.converted_file_path: pathlib.Path = None
        self.status = FileStatus.UNCONVERTED

    def get_name(self) -> str:
        return self.full_name.strip("." + self.get_extension())
       
    def get_extension(self) -> str:
        return self.full_name.split(".")[-1]

    def get_status(self) -> FileStatus:       
        return self.status

    def file_exists(self) -> bool:
        return self.file_path.is_file()





