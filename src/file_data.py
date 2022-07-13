
import pathlib

class FileData:
    def __init__(self, path:str, name:str, file_extension:str) -> None:
        self.file_path = path
        self.full_name = name
        self.file_extension = file_extension
     
        self.converted = False
        self.converted_file_path = ""

    def get_status(self)-> str:
        self.converted = self.find_converted_file_path()
        if not self.converted :
            self.converted_file_path = ""

        return "Converted" if self.converted else "Unconverted"
    
    def get_label(self)-> str:
        return self.full_name

    def get_name(self)-> str:
        return self.full_name.strip("." + self.file_extension)

    def get_extension(self)->str:
        return self.file_extension
    
    def get_file_path(self)-> str:
        return self.file_path
    
    def find_converted_file_path(self)-> bool:
        path = pathlib.Path(self.converted_file_path)
        return path.is_file()
        


   


