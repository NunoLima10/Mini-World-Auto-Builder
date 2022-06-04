
from voxel_data import VoxelData
class ConverterManager:
    def __init__(self) -> None:
        self.file_type = [("Voxel Data Files","*.txt","*vox")]
        self.voxel_data_files = []
        self.file_labels = []

    def add_file(self, file_path:str)-> list:
        new_voxel_data_file = VoxelData(file_path)
        self.file_labels.append(new_voxel_data_file.name)
        self.voxel_data_files.append(new_voxel_data_file)
        return self.file_labels


    def find_file_by_name(self,name:str)-> VoxelData:
        pass

            
