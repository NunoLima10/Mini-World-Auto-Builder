
import pathlib
import PySimpleGUI as sg

from file_data import FileData
from voxel_converter import VoxelConverter

class ConverterManager:
    def __init__(self,icon:str) -> None:
        self.icon = icon 
        #self.file_type = [("Voxel Data Files","*.txt","*vox")]
        self.file_extensions = ["txt","vox"]
        self.file_type = [("Voxel Data Files","*vox")]

        self.files_data = []
        self.selected_file = None

        self.initial_folder = pathlib.Path.cwd()
        self.output_folder = self.initial_folder

    def find_file_by_name(self, name:str)-> FileData:
        for file_data in self.files_data:
            if file_data.full_name == name:
                return file_data
        return None #add not find exeption
    
    def get_files_lables(self)-> list:
        return [file.get_label() for file in self.files_data]


    def get_new_file(self)-> None:
        path = sg.popup_get_file("File",no_window=True ,file_types=self.file_type, icon=self.icon,initial_folder=self.initial_folder)
        file_path = pathlib.Path(path)

        if file_path.is_file():
            file_name = file_path.name
            file_extension = file_name.split(".")[-1]
            file = self.find_file_by_name(file_name)

            if file is None:
                new_file_data = FileData(file_path, file_name, file_extension)
                self.files_data.append(new_file_data)
                

    def set_output_folder(self)-> None:
           path = sg.popup_get_folder("Folder", no_window=True, icon=self.icon, initial_folder=self.initial_folder)
           folder_path = pathlib.Path(path)
           if folder_path.is_dir():
               self.output_folder = folder_path
 

    def get_file_status(self, file_name:str)-> str:
        voxeldata = self.find_file_by_name(file_name)
        return voxeldata.get_status()

    def set_file_for_conversion(self, file_name:str)-> None:
        self.selected_file = self.find_file_by_name(file_name)

    def convert_file(self)-> None:
        if self.selected_file is None: return

        file_extension = self.selected_file.get_extension()
        try:
            if file_extension == "vox":
                file_converted = VoxelConverter(self.selected_file,self.output_folder)
                
        except FileNotFoundError:
            print("ficehiro não encontrado")


  
        

            
