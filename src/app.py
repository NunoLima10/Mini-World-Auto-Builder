
import PySimpleGUI as sg

from layout import Layout
from langues import Language
from converter_manager import ConverterManager
from open_url import open_page_url

class App:
    def __init__(self,title: str, size: tuple, icon:str, language:str) -> None:
        self.title = title
        self.size = size 
        self.icon = icon

        self.language = Language(language)
        self.language_data = self.language.get_language_data()
        self.languages_labels = self.language.get_languages_labels()

        self.layout = Layout(self.language_data, self.languages_labels)
        self.font = self.layout.font

        self.converter_manager = ConverterManager(self.icon)

        self.create_window()

        self.events = {
            "-RUN-":self.convert_voxel_data,
            "-FINDFILE-":self.open_get_file,
            "-LISTBOX-" :self.set_file_status,
            self.language_data["Find File"]: self.open_get_file,
            self.language_data["Output Folder"]: self.change_output_folder,
            self.language_data["Tutorial"]: self.open_page,
            self.language_data["Online Voxelizer"]: self.open_page,
            self.language_data["YouTube Channel"]: self.open_page,
            self.language_data["Repository"]: self.open_page,
            self.language_data["Version"]: self.open_version_popup,
        }

    def create_window(self)->None:
        window_layout = self.layout.build_layout()
        self.window = sg.Window(self.title, window_layout, size=self.size, icon=self.icon)
        self.window.BackgroundColor = self.layout.palette["Color1"]

    def open_get_file(self, event)-> None:
        self.converter_manager.get_new_file()
        self.window["-LISTBOX-"].update(values=self.converter_manager.file_labels)

    def change_output_folder(self, event)-> None:
         self.converter_manager.set_output_folder()

    def set_file_status(self,event)-> None:
        
        print(self.values["-LISTBOX-"])

    def convert_voxel_data(self,event)-> None:
        #self.values["-LISTBOX-"]
        print("convert")


  
        
    
    def open_page(self,event)-> None:
        open_page_url(event)
        
    
    def open_version_popup(self,event)-> None:
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
                event_function = self.events[event]
                event_function(event)
               
            if event in self.languages_labels:
                self.change_language(event)

    def close(self)-> None:
        self.window.close()


