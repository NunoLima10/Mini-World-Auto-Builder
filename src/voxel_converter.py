import pathlib
import time


from file_data import FileData
from utils import color_distance,block_color_data
from voxel_parser import VoxParser
from pallete import Pallete
from Exceptions import FileNotFoundException

BASE_CODE_PATH = pathlib.Path('.\\assets\\lua_base_code.txt')
class VoxelConverter:
    def __init__(self, file_data: FileData, output_folder: pathlib.Path, pallete: Pallete) -> None:
        self.file_data = file_data
        self.output_folder =  output_folder

        self.pallete = pallete
      
        
    def load_voxel_data(self) -> None:
        if not self.file_data.file_exists(): 
            raise FileNotFoundException("File not found")    

        self.voxel_data = VoxParser(self.file_data.file_path)
        self.voxel_data.import_vox(self.pallete)
        
           

    def generate_position_table(self) -> str:
        voxels = self.voxel_data.voxels
        position_table = 'positions = {'
     
        for voxel in voxels:
            position_line = '{'+f'{voxel.x},{voxel.y},{voxel.z},{voxel.c}'+'}'
            position_table = position_table + position_line + ','

        return position_table.strip(',') + '}'

    def get_block_list(self) -> list[tuple]:
        color_data = self.voxel_data.palette
        block_list = []
        processed_colors = {}

        for color in color_data:
            if str(color) not in processed_colors:
                block = block_color_data[0]
                mim_delta_E = color_distance((color.r,color.g,color.b),(block.r,block.g,block.b))

                for block in block_color_data:
                    delta_E = color_distance((color.r,color.g,color.b),(block.r,block.g,block.b)) 

                    if mim_delta_E >= delta_E:
                        mim_delta_E = delta_E
                        mim_delta_E_block = block

                block_list.append(mim_delta_E_block)

                processed_colors[str(color)] = mim_delta_E_block    
                continue     
            block_list.append(processed_colors[str(color)])

        return block_list

    def generate_block_table(self) -> str:
        block_list = self.get_block_list()
        blocks_table = "blocks = {"

        for block in block_list:
            block_line = '{'+f'{block.block_id},{block.color_data}'+'}'
            blocks_table = blocks_table + block_line + ','

        return blocks_table.strip(',') + '}'

    
    def get_postion_label(voxel:tuple)->str:
        return f"{voxel.x},{voxel.y},{voxel.z}"

    def get_color_info(self, voxel:tuple)->tuple:
        return self.voxel_data.palette[voxel.c]

    def convert_file(self) -> pathlib.Path:

        self.load_voxel_data()

        postions = self.generate_position_table()
        blocks = self.generate_block_table()
        base_code = BASE_CODE_PATH.read_text()

        lua_script =  f"{postions}\n {blocks}\n {base_code}"

        file_name = self.file_data.get_name() + ".txt"

        path = self.output_folder.joinpath(file_name)
        
        
        path.write_text(lua_script)
        
        return path
        
       


