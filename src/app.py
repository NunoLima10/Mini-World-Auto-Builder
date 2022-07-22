
import PySimpleGUI as sg
import math 

from layout import Layout
from langues import Language
from converter_manager import ConverterManager
from pallete import Pallete
from open_url import open_page_url
from popup_controller import Popup

class App:
    def __init__(self, title: str, size: tuple, icon: str, language: str) -> None:
        self.title = title
        self.size = size 
        self.icon = icon


        self.language = Language(language)
        self.language_data = self.language.get_language_data()
        self.languages_labels = self.language.get_languages_labels()

        self.animation_frame = 0
        self.converting = False
        
        self.layout = Layout(self.language_data, self.languages_labels)
        self.font = self.layout.get_font()

        self.pallete = Pallete(icon, pallete_path='.\\assets\\Mini_World_color_pallete.png')
        self.converter_manager = ConverterManager(self.icon, self.pallete)

        self.popup = Popup(self.icon,(400,150))

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
            self.language_data["Select Palette"]: self.set_defaut_pallete,
        }

    def create_window(self) -> None:
        window_layout = self.layout.build_layout()
        self.window = sg.Window(self.title, window_layout, size=self.size, icon=self.icon, background_color=self.layout.palette["Color1"])
     

    def open_get_file(self, **kwarg) -> None:
        self.converter_manager.get_new_file()
        self.window["-LISTBOX-"].update(values=self.converter_manager.get_files_lables())

    def change_output_folder(self, **kwarg)-> None:
         self.converter_manager.set_output_folder()


    def set_file_status(self, **kwarg)-> None:
        if len(self.values["-LISTBOX-"]) == 0: return
        file_name = self.values["-LISTBOX-"][0]
        animation = ["",".","..","..."]

        status = self.converter_manager.get_file_status(file_name)
       

        if status == "Converting":
            frame = math.floor(self.animation_frame % 4)
            self.window["-STATUS-"].Update(self.language_data["Converting"] + animation[frame])
            self.animation_frame += 0.1
        else:
            status_label = f'{file_name} >> {self.language_data[status]}'
            self.window["-STATUS-"].Update(status_label)

    def convert_voxel_data(self, **kwarg) -> None:

        if len(self.values["-LISTBOX-"]) == 0: return

        file_name = self.values["-LISTBOX-"][0]

        self.converter_manager.set_file_for_conversion(file_name)
        
        self.window.perform_long_operation(self.converter_manager.convert_file,"--CONVERTION_END--")
        self.converting = True
       
        
    def open_page(self, **kwarg) -> None:
        for key,value in self.language_data.items():
            if kwarg["event"] ==  value:
               url_key = key 
               break
        open_page_url(url_key)
        
    
    def set_defaut_pallete(self, **kwarg) -> None: 
       
        self.converter_manager.pallete = self.pallete

    def open_version_popup(self,event)-> None:
        print("open_version_popup")
    

    def change_language(self, language_Label: str) -> None:

        if self.converting: return

        self.language_data = self.language.change_language(language_Label)
        self.layout = Layout(self.language_data, self.languages_labels)

        self.close()
        self.create_window()

        _, self.values = self.window.read(timeout=20)
        self.window["-LISTBOX-"].update(values=self.converter_manager.get_files_lables())
        self.window["-STATUS-"].update(self.language_data["Status"])
            

    def run(self)-> None:
        
        while True:
            app_event, self.values = self.window.read(timeout=20)

            if app_event == sg.WIN_CLOSED or app_event == self.language_data["Exit"]:
                break
               
            if app_event in self.events:
                event_function = self.events[app_event]
                event_function(event = app_event)
                
            if app_event in self.languages_labels:
                self.change_language(app_event)

            if self.converting:
                self.set_file_status()
            
            if app_event == "--CONVERTION_END--":

                conversion_status = self.values["--CONVERTION_END--"]
                self.converting = False

                if conversion_status == "ok":
                    self.converter_manager.finished_conversation()
                    self.set_file_status()
                else:
                    self.popup.show("",self.language_data[conversion_status],"ok")
               
                         
    def close(self)-> None:
        self.window.close()


