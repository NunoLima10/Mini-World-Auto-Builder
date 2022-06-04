
class VoxelData:
    def __init__(self, path:str) -> None:
        self.file_path = path
        self.name = path.split("/")[-1]
        self.file_type = self.name.split(".")
        
        
        self.converted = False
        self.converted_file_path = ""

    def get_status(self)-> str:
        self.converted = self.find_converted_file_path()
        return "Converted" if self.converted else "Unconverted"
    


    def find_converted_file_path(self)-> bool:
        pass




   


