
import pathlib
import PySimpleGUI as sg

from PIL import Image
from utils import FileNotFoundException

class PalletSizeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Pallete:
    def __init__(self, icon: str, pallete_path: str) -> None:
        self.file_path = pathlib.Path(pallete_path)
        
        self.file_type = [("Palette file","*.png")]
        self.initial_folder = pathlib.Path.cwd()
        self.icon = icon      
        
    def load(self) -> None:
        if not self.file_path.is_file():
            raise FileNotFoundException

        self.image = Image.open(self.file_path)
        self.width, self.height = self.image.size

        self.pixels = list(self.image.getdata())

        if self.width  > 256 or self.height > 1 :
            raise PalletSizeException

    def get_pattlete(self) -> None:
        path = sg.popup_get_file("File", no_window=True, file_types=self.file_type, 
                                icon=self.icon, initial_folder=self.initial_folder)
        self.file_path = pathlib.Path(path)

        
               
