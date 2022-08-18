
import PySimpleGUI as sg
import math 

from src.config import AppConfig
from src.langues import Language
from src.layout import Layout
from src.popup import Popup
from src.pallete import Pallete
from src.converter_manager import ConverterManager
from src.browser import Browser

class App:
    def __init__(self) -> None:

        self.app_config = AppConfig()
        self.converting = False
        self.app_set_up()
    
    #set up

    def app_set_up(self) -> None:
        self.language_set_up()
        self.layout_set_up()
        self.window_set_up()
        self.popup_set_up()

        self.pallete_set_up()
        self.converter_set_up()

        self.event_set_up()
        self.bowser_set_up()
        self.animation_set_up()
        
    def language_set_up(self) -> None:
        language_id = self.app_config.config["Language"]

        self.language = Language(language_id)
        self.language_data = self.language.language_data
        self.languages_labels = self.language.get_languages_labels()
       
    def layout_set_up(self) -> None:
        self.layout = Layout(self.language_data, self.languages_labels)

    def window_set_up(self) -> None:
        title = self.app_config.config["Title"]
        window_size = int(self.app_config.config["Window Size"])
        icon = self.app_config.config["Icon Path"]

        window_layout = self.layout.build_layout()

        self.window = sg.Window(
            title, 
            window_layout, 
            size=(window_size,  window_size),
            icon=icon, 
            background_color=self.layout.palette["Color1"]
        )

        self.window.read(timeout=20)
        self.window["-CONVERT-"].set_cursor("hand2")
        self.window["-SELECT_FILE-"].set_cursor("hand2")
        self.window["-PALLETE_ICON-"].set_cursor("hand2")

    def popup_set_up(self) -> None:
        width = 400
        height = 150
        icon = self.app_config.config["Icon Path"]
        self.popup = Popup(icon, (width,height))

    def pallete_set_up(self) -> None:
        pallete_path = self.app_config.config["Pallete"]
        icon = self.app_config.config["Icon Path"]

        self.pallete = Pallete(icon)
        load_status = self.pallete.load(pallete_path)

        if load_status == "Success":
            self.window["-PALLETE_IMG-"].update(visible=True) 
            self.window["-PALLETE_IMG-"].update(data=self.pallete.get_resized_pallete()) 
            return 
        self.popup.show(
            title=self.language_data["Warning"],
            description=self.language_data[load_status], 
            button_text=self.language_data["ok"]
        )

    def converter_set_up(self) -> None:
        self.converter_manager = ConverterManager(self.app_config, self.pallete)

    def event_set_up(self) -> None:
        self.events = {
            "-CONVERT-": self.convert,
            "-SELECT_FILE-": self.select_file,
            "-LISTBOX-" : self.update_file_status,
            "-PALLETE_ICON-": self.select_pallete,
            self.language_data["Find File"]: self.select_file,
            self.language_data["Output Folder"]: self.change_output_folder,
            self.language_data["Tutorial"]: self.open_page,
            self.language_data["Online Voxelizer"]: self.open_page,
            self.language_data["YouTube Channel"]: self.open_page,
            self.language_data["Repository"]: self.open_page,
        }
    
    def bowser_set_up(self) -> None:
        self.bowser =  Browser()

    def animation_set_up(self) -> None:
        self.animation_frame = 0
        self.animation = ["",".","..","..."]
    
    #events

    def convert(self, **kwarg) -> None:
        if len(self.values["-LISTBOX-"]) == 0: 
            return

        file_name = self.values["-LISTBOX-"][0]
        self.converter_manager.set_file_for_conversion(file_name)

        key = "--CONVERTION_END--"
        self.window.perform_long_operation(self.converter_manager.convert_file, key)
        self.converting = True

    def select_file(self, **kwarg) -> None:
        self.converter_manager.get_new_file()
        new_labels = self.converter_manager.get_files_labels()
        self.window["-LISTBOX-"].update(values=new_labels)

    def update_file_status(self, **kwarg) -> None:
        if len(self.values["-LISTBOX-"]) == 0: 
            return

        file_name = self.values["-LISTBOX-"][0]
        status = self.converter_manager.get_file_status(file_name)

        if status == "Converting":
            frame = math.floor(self.animation_frame % 4)
            status_text = self.language_data["Converting"] + self.animation[frame]
            self.animation_frame += 0.1
        else:
            status_text = f'{file_name} >> {self.language_data[status]}'
        self.window["-STATUS-"].Update(status_text)

    def select_pallete(self, **kwarg) -> None: 
        load_status = self.pallete.get_pallete()

        if load_status == "Success":
            self.window["-PALLETE_IMG-"].update(data=self.pallete.get_resized_pallete())
            return 
        self.popup.show(
            title=self.language_data["Warning"],
            description=self.language_data[load_status], 
            button_text=self.language_data["ok"]
        )

    def change_output_folder(self, **kwarg) -> None:
        self.converter_manager.set_output_folder()
    
           
    def open_page(self, **kwarg) -> None:
        for key,value in self.language_data.items():
            if kwarg["event"] ==  value:
               url_key = key 
               break
        self.bowser.open_page(url_key)
          

    def change_language(self, language_Label: str) -> None:
        if self.converting: 
            self.popup.show(
                title=self.language_data["Warning"],
                description=self.language_data["CannotChangeLanguage"],
                button_text=self.language_data["ok"]
            )
            return
        
        self.language.change_language(language_Label)
        self.language_data = self.language.language_data
        self.languages_labels = self.language.get_languages_labels()
        
        self.layout = Layout(self.language_data, self.languages_labels)

        self.event_set_up()

        self.close()
        self.window_set_up()
        self.pallete_set_up()

        _, self.values = self.window.read(timeout=20)
        self.window["-LISTBOX-"].update(values=self.converter_manager.get_files_labels())
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
                self.update_file_status()
            
            if app_event == "--CONVERTION_END--":
                self.converting = False

                conversion_status = self.values["--CONVERTION_END--"]
                if conversion_status:
                    if conversion_status == "Success":
                        self.converter_manager.finished_conversation()
                        self.update_file_status()
                    else:
                        self.popup.show(
                            title=self.language_data["Warning"],
                            description=self.language_data[conversion_status],
                            button_text=self.language_data["ok"]
                        )        

    def save_config(self) -> None:
        self.app_config.config["Import"] = self.converter_manager.import_folder
        self.app_config.config["Export"] = self.converter_manager.export_folder
        self.app_config.config["Pallete"] = self.pallete.file_path
        self.app_config.config["Language"] = self.language.language_id

        self.app_config.save()

    def close(self)-> None:
        self.save_config()
        self.window.close()


