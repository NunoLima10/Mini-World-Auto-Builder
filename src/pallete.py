
import PySimpleGUI as sg
import pathlib

from io import BytesIO
from PIL import Image
from src.exceptions import FileNotFoundException,PalletSizeException


class Pallete:
    def __init__(self, icon: str) -> None:

        self.file_path: pathlib.Path = None
        
        self.file_type = [("Palette file","*.png")]
        self.initial_folder = pathlib.Path.cwd()
        self.icon = icon      
        
    def parser(self, path: str) -> None:
        file_path = pathlib.Path(path)

        if not file_path.is_file():
            raise FileNotFoundException

        self.image = Image.open(file_path)
        self.image.convert("RGBA")
        self.width, self.height = self.image.size

        self.pixels = list(self.image.getdata())

        if self.width != 256 or self.height != 1 :
            raise PalletSizeException

    def load(self, path: pathlib.Path) -> str:
        try:
            self.parser(path)
            self.file_path = path
            return "Success"
        except FileNotFoundException:
            return "FileNotFoundException"
        except PalletSizeException:
            return "PalletSizeException"

    def get_resized_pallete(self) -> None:
        bio =  BytesIO()
        new_image = self.image.resize((380,20))

        new_image.save(bio,format='PNG')

        return bio.getvalue()

    def get_pallete(self) -> str:
        path = sg.popup_get_file(
                    "File", 
                    no_window=True, 
                    file_types=self.file_type, 
                    icon=self.icon, 
                    initial_folder=self.initial_folder
                )
        file_path = pathlib.Path(path)
        return self.load(file_path)

    def valid_path(self) -> bool:
        if self.file_path:
            return self.file_path.is_file()

        


        
               
