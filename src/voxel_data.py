
class VoxelData:
    def __init__(self, path:str, name:str, file_extension:str) -> None:
        self.file_path = path
        self.name = name
        self.file_extension = file_extension
        
        
        self.converted = False
        self.converted_file_path = ""

    def get_status(self)-> str:
        self.converted = self.find_converted_file_path()
        return "Converted" if self.converted else "Unconverted"
    


    def find_converted_file_path(self)-> bool:
        pass




   


