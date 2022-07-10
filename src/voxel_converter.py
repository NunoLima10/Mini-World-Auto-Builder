from pyvox.parser import VoxParser

class VoxelConverter:
   def __init__(self, path:str, name:str, file_extension:str) -> None:
        self.file_path = path
        self.name = name
        self.file_extension = file_extension
        self.file_data = VoxParser(self.file_path)
        
        
        self.converted = False
        self.converted_file_path = ""
        