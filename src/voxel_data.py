
class VoxelData:
    def __init__(self, path:str) -> None:
        self.file_path = path
        self.name = path.split("/")[-1]
        self.file_type = self.name.split(".")
        
        self.converted = False
        self.converted_file_path = ""