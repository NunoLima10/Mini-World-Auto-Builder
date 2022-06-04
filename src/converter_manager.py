import pathlib
import PySimpleGUI as sg

from voxel_data import VoxelData

class ConverterManager:
    def __init__(self,icon:str) -> None:
        self.icon = icon 
        #self.file_type = [("Voxel Data Files","*.txt","*vox")]
        self.file_extensions = ["txt","vox"]
        self.file_type = [("Voxel Data Files","*vox")]

        self.voxel_data_files = []
        self.file_labels = []


        self.initial_folder = pathlib.Path.cwd()
        self.output_folder = self.initial_folder

    def get_new_file(self)-> None:
        path = sg.popup_get_file("File",no_window=True ,file_types=self.file_type, icon=self.icon,initial_folder=self.initial_folder)
        file_path = pathlib.Path(path)

        if file_path.is_file():
            file_name = file_path.name
            file_extension = file_name.split(".")[-1]

            if file_name not in self.file_labels:
                new_voxel_data_file = VoxelData(file_path, file_name, file_extension)
                self.voxel_data_files.append(new_voxel_data_file)
                self.file_labels.append(file_name)

    def set_output_folder(self)-> None:
           path = sg.popup_get_folder("Folder", no_window=True, icon=self.icon, initial_folder=self.initial_folder)
           folder_path = pathlib.Path(path)
           if folder_path.is_dir():
               self.output_folder = folder_path
 


    def find_file_by_name(self,name:str)-> VoxelData:
        for voxel_data in self.voxel_data_files:
            if voxel_data.name == name:
                return voxel_data
        return None


            
