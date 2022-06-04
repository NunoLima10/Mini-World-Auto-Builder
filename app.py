from optparse import Values
import PySimpleGUI as sg

from layout import Layout
from langues import Language
from converter_manager import ConverterManager

class App:
    def __init__(self,title: str, size: tuple, icon:str,language:str) -> None:
        self.title = title
        self.size = size 
        self.icon = icon

        self.language = Language(language)
        self.language_data = self.language.get_language_data()
        self.languages_labels = self.language.get_languages_labels()

        self.layout = Layout(self.language_data, self.languages_labels)
        self.font = self.layout.font


        self.converter_manager = ConverterManager()

        self.create_window()



        self.events = {
            "-RUN-":self.convert_voxel_data,
            "-FINDFILE-":self.open_find_file,
            self.language_data["Find File"]:self.open_find_file,
            self.language_data["Tutorial"]:self.open_url,
            self.language_data["Online Voxelizer"]:self.open_url,
            self.language_data["YouTube Channel"]:self.open_url,
            self.language_data["Repository"]:self.open_url,
            self.language_data["Version"]:self.open_version_popup,
        }

        
        
    def create_window(self)->None:
        window_layout = self.layout.build_layout()
        self.window = sg.Window(self.title, window_layout, size = self.size, icon = self.icon)
        self.window.BackgroundColor = self.layout.palette["Azul1"]



    def convert_voxel_data(self)-> None:
        print(self.values["-LISTBOX-"])


    def open_find_file(self)-> None:
        file_types = self.converter_manager.file_type
        file_path = sg.popup_get_file("File",no_window=True ,file_types=file_types,icon=self.icon)
        new_file_labels = self.converter_manager.add_file(file_path)

        self.window["-LISTBOX-"].update(values=new_file_labels)
        
        
    
    def open_url(self)-> None:
        print("open_url")
    
    def open_version_popup(self)-> None:
        print("open_version_popup")
    

    def change_language(self,language_Label:str)-> None:
            self.language_data = self.language.change_language(language_Label)
            self.layout = Layout(self.language_data,self.languages_labels)
            self.close()
            self.create_window()


    def run(self)-> None:
        while True:
            event,self.values = self.window.read()

            if event == sg.WIN_CLOSED or event== self.language_data["Exit"] :
                break

           

            if event in self.events:
                self.events[event]

            if event in self.events:
                self.events[event]()
               
            
            if event in self.languages_labels:
                self.change_language(event)

    def close(self)-> None:
        self.window.close()


