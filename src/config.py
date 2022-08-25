from configparser import ConfigParser

import pathlib

class AppConfig:
    def __init__(self) -> None:
        self.config_paser =  ConfigParser()
        self.file_path = pathlib.Path('.\\config\\config.ini')

        self.load_config()
        
    def generate_export_folder(self, import_folder: pathlib.Path ) -> pathlib.Path:
        folder_name = "lua_scripts"
        export_folder = import_folder.joinpath(folder_name)

        if not pathlib.Path.exists(export_folder):
            export_folder.mkdir()
        return export_folder

    def generate_default_config(self) -> ConfigParser:
        default_config = ConfigParser()

        title = 'MiniWorld-AutoBuilder'
        size = "500"
        icon_path = "assets\icon_logo.ico"
        language_id = "en"

        pallete_path = 'pallete\\Mini_World_color_pallete.png'
        import_folder = pathlib.Path.cwd()
        export_folder = self.generate_export_folder(import_folder)
        lua_base_code = '.\\assets\\lua_base_code.txt'

        default_config.add_section('UI')
        default_config.set('UI','Title',title)
        default_config.set('UI','Window Size',size)
        default_config.set('UI','Icon Path',icon_path)

        default_config.add_section('Language')
        default_config.set('Language','Id',language_id)

        default_config.add_section('Pallete')
        default_config.set('Pallete','Path',pallete_path)

        default_config.add_section('Export')
        default_config.set('Export','Path',str(export_folder))

        default_config.add_section('Import')
        default_config.set('Import','Path',str(import_folder))

        default_config.add_section('Lua Base Code')
        default_config.set('Lua Base Code','Path',lua_base_code)

        return default_config

    def load_config(self) -> None:
        if pathlib.Path.exists(self.file_path):
            self.config_paser.read(self.file_path)
        else:
            self.config_paser = self.generate_default_config()

        self.config = {
            "Title": self.config_paser["UI"]["Title"],
            "Language":self.config_paser["Language"]["Id"],
            "Icon Path": pathlib.Path(self.config_paser["UI"]["Icon Path"]),
            "Pallete":pathlib.Path(self.config_paser["Pallete"]["Path"]),
            "Export": pathlib.Path(self.config_paser["Export"]["Path"]),
            "Import": pathlib.Path(self.config_paser["Import"]["Path"]),
            "Lua Code" :pathlib.Path(self.config_paser["Lua Base Code"]["Path"]),     
            "Window Size":(int(self.config_paser["UI"]["Window Size"])) 
        }
        self.valid_config()
                
    def save(self) -> None:
        pallete_path = self.config["Pallete"]
        export_folder = self.config["Export"]
        import_folder = self.config["Import"]
        language_id = self.config["Language"]

        self.config_paser.set('Pallete','Path',str(pallete_path))
        self.config_paser.set('Export','Path',str(export_folder))
        self.config_paser.set('Import','Path',str(import_folder))
        self.config_paser.set('Language','Id',language_id)

        with open(self.file_path,"w") as configfile:
            self.config_paser.write(configfile)

    def valid_config(self) -> None:
        defaut_config = self.generate_default_config()

        pallete_path: pathlib.Path = self.config["Pallete"]
        export_folder: pathlib.Path = self.config["Export"]
        import_folder: pathlib.Path = self.config["Import"]

        if not pathlib.Path.exists(pallete_path):
           self.config["Pallete"] = defaut_config["Pallete"]["Path"]

        if not pathlib.Path.exists(export_folder):
           self.config["Export"] = defaut_config["Export"]["Path"]
        
        if not pathlib.Path.exists(import_folder):
           self.config["Import"] = defaut_config["Import"]["Path"]
        
        

        

