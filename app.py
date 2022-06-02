
from re import S
import PySimpleGUI as sg

from layout import build_layout,PALETTE,FONT
from langues import get_language_data,available_languages

class App:
    def __init__(self,title: str, size: tuple, icon:str = None,language:str = "pt") -> None:
        self.title = title
        self.size = size 
        self.icon = icon
        self.language = language
        self.font = FONT


        self.language_data = get_language_data(self.language)  
        self.available_languages = available_languages

        self.layout = build_layout(self.language_data, self.available_languages)
        self.create_window()



        self.events = {
            "-RUN-":self.generate_script,
            "-FINDFILE-":self.open_find_file,
            self.language_data["Find File"]:self.open_find_file,
            self.language_data["Tutorial"]:self.open_url,
            self.language_data["Online Voxelizer"]:self.open_url,
            self.language_data["YouTube Channel"]:self.open_url,
            self.language_data["Repository"]:self.open_url,
            self.language_data["Version"]:self.open_version_popup,
        }

        
        
    def create_window(self)->None:
        self.window = sg.Window(self.title, self.layout, size = self.size, icon = self.icon)
        self.window.BackgroundColor = PALETTE["Azul1"]



    def generate_script(self)-> None:
        print("generate_script")

    def open_find_file(self)-> None:
        print("open_find_file")
    
    def open_url(self,)-> None:
        print("open_url")
    
    def open_version_popup(self)-> None:
        print("open_version_popup")
    

    def change_language(self,language)-> None:
        if self.available_languages[language] != self.language:

            self.language = self.available_languages[language]
            self.language_data = get_language_data(self.language)
            self.layout = build_layout(self.language_data, self.available_languages)
            self.close()
            self.create_window()


    def run(self)-> None:
        while True:
            event,values = self.window.read()

            if event == sg.WIN_CLOSED or event== self.language_data["Exit"] :
                break

            if event in self.events:
                self.events[event]

            if event in self.events:
                self.events[event]()
            
            if event in self.available_languages:
                self.change_language(event)

    def close(self)-> None:
        self.window.close()


