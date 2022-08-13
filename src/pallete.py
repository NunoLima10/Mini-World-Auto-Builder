
import pathlib
import PySimpleGUI as sg
from io import BytesIO

from PIL import Image
from exceptions import FileNotFoundException,PalletSizeException



class Pallete:
    def __init__(self, icon: str, pallete_path: str) -> None:
        self.file_path = pathlib.Path(pallete_path)
        
        self.file_type = [("Palette file","*.png")]
        self.initial_folder = pathlib.Path.cwd()
        self.icon = icon      
        
    def load(self, path: pathlib.Path = None) -> None:
        if not path:
            path = self.file_path

        if not path.is_file():
            raise FileNotFoundException

        self.image = Image.open(path)
        self.image.convert("RGBA")
        self.width, self.height = self.image.size

        self.pixels = list(self.image.getdata())

        if self.width != 256 or self.height != 1 :
            raise PalletSizeException

    def get_resized_pallete(self) -> None:
        bio =  BytesIO()
        new_image = self.image.resize((380,20))

        new_image.save(bio,format='PNG')

        return bio.getvalue()




    def get_pallete(self) -> str:
        path = sg.popup_get_file("File", no_window=True, file_types=self.file_type, 
                                icon=self.icon, initial_folder=self.initial_folder)
        file_path = pathlib.Path(path)

        try:
            self.load(file_path)
            self.file_path = file_path
            return "Success"
        except FileNotFoundException:
            return "FileNotFoundException"
        except PalletSizeException:
            return "PalletSizeException"


        
               
