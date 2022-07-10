
import PySimpleGUI as sg

from layout import Layout
from langues import Language
from converter_manager import ConverterManager
from open_url import open_page_url

class App:
    def __init__(self, title: str, size: tuple, icon:str, language:str) -> None:
        self.title = title
        self.size = size 
        self.icon = icon

        self.language = Language(language)
        self.language_data = self.language.get_language_data()
        self.languages_labels = self.language.get_languages_labels()
   

        self.layout = Layout(self.language_data, self.languages_labels)
        self.font = self.layout.get_font()

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

    def open_get_file(self, **kwarg)-> None:
        self.converter_manager.get_new_file()
        self.window["-LISTBOX-"].update(values=self.converter_manager.get_files_lables())

    def change_output_folder(self, **kwarg)-> None:
         self.converter_manager.set_output_folder()

    def set_file_status(self, **kwarg)-> None:
        if len(self.values["-LISTBOX-"]) == 0: return
        file_name = self.values["-LISTBOX-"][0]
    
        status = self.converter_manager.get_file_status(file_name)
        self.window["-STATUS-"].Update(self.language_data[status])

    def convert_voxel_data(self, **kwarg)-> None:
        if len(self.values["-LISTBOX-"]) == 0: return
        file_name = self.values["-LISTBOX-"][0]
        
    def open_page(self,**kwarg)-> None:
        for key,value in self.language_data.items():
            if kwarg["event"] ==  value:
               url_key = key 
               break
        open_page_url(url_key)
        
    
    def open_version_popup(self,event)-> None:
        print("open_version_popup")
    

    def change_language(self,language_Label:str)-> None:
            self.language_data = self.language.change_language(language_Label)
            self.layout = Layout(self.language_data,self.languages_labels)

            self.close()
            self.create_window()

            _,self.values = self.window.read(timeout=20)
            self.window["-LISTBOX-"].update(values=self.converter_manager.get_files_lables())
            self.window["-STATUS-"].update(self.language_data["Status"])
            

    def run(self)-> None:
        while True:
            app_event,self.values = self.window.read(timeout=20)

            if app_event == sg.WIN_CLOSED or app_event == self.language_data["Exit"] :
                break
               
            if app_event in self.events:
                event_function = self.events[app_event]
                event_function(event = app_event)
                
            if app_event in self.languages_labels:
                self.change_language(app_event)
            
            
                

    def close(self)-> None:
        self.window.close()


