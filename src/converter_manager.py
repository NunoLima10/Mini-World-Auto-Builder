
import pathlib
import PySimpleGUI as sg

from file_data import FileData,FileStatus
from voxel_converter import VoxelConverter
from voxel_parser import VoxPaserException

class ConverterManager:
    def __init__(self, icon: str) -> None:
        self.icon = icon 
        self.file_extensions = ["txt","vox"]
        self.file_type = [("Voxel Data Files","*.vox")]

        self.files_data = {}
        self.selected_file = None
    
        self.initial_folder = pathlib.Path.cwd()
        self.output_folder = self.initial_folder

    def get_new_file(self) -> None:
        path = sg.popup_get_file("File", no_window=True, file_types=self.file_type, icon=self.icon, initial_folder=self.initial_folder)
        file_path = pathlib.Path(path)

        if file_path.is_file():
                new_file_data = FileData(file_path)
                self.files_data[new_file_data.full_name] = new_file_data


    def find_file_by_name(self, full_name: str) -> FileData:
        return self.files_data[full_name] if full_name in self.files_data else None

    def get_files_lables(self)-> list:
        return  self.files_data.keys()
    
    def get_file_status(self, full_name: str) -> str:
        status = self.find_file_by_name(full_name).get_status()
        return status.value
      
    def set_file_for_conversion(self, full_name: str) -> None:
        self.selected_file = self.find_file_by_name(full_name)
      
    def convert_file(self) -> None:
        if not self.selected_file: 
            return
        if not self.selected_file.status == FileStatus.UNCONVERTED: 
            return
        full_name = self.selected_file.full_name

        file_extension = self.selected_file.get_extension()
        try:
            if file_extension == "vox":
                file_converted = VoxelConverter(self.selected_file,self.output_folder)

                self.files_data[full_name].status = FileStatus.CONVERTING
                output_file_path = file_converted.convert_file() 
                
                self.files_data[full_name].converted_file_path = output_file_path

        except FileNotFoundError:
            del self.files_data[full_name]
            self.selected_file = None

        except VoxPaserException:
            self.files_data[full_name].status = FileStatus.NOT_SUPPORTED
            self.selected_file = None

    def finished_conversation(self) -> None:
        full_name = self.selected_file.full_name
        self.files_data[full_name].status = FileStatus.CONVERTED
        self.selected_file = None

    def set_output_folder(self) -> None:
           path = sg.popup_get_folder("Folder", no_window=True, icon=self.icon, initial_folder=self.initial_folder)
           folder_path = pathlib.Path(path)
           if folder_path.is_dir():
               self.output_folder = folder_path

  
        

            
