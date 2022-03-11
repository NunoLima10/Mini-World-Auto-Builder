__author__="Nuno Lima"
__copyright__="Copyright 2022 Nuno Lima"
__version__="0.0.1"
__maintainer__="Nuno Lima"
__email__="contato.playcraft@gmail.com"
__status__="Production"

#global

data_path='voxel_data.txt'
block_data_path='block_data.txt'
lua_script_path='lua_script.txt'
base_code_path='lua_base_code.txt'

#file management

def read_txt_file(path):
    with open(path,"r") as file_data:  
        return file_data.readlines()

def get_line_data(line,data_index):
    index_1,index_2,index_3=data_index
    line_data=[text.replace(' ','') for text in line]
    return f"{line_data[index_1]},{line_data[index_2]},{line_data[index_3]}"    

def text_to_num_list(text_data,separator):
    text_data=text_data.strip('\n')   
    text_data=text_data.split(separator)
    return[int(value) for value in text_data if value.isnumeric()]

def get_block_data():
    block_data=read_txt_file(block_data_path)
    return [text_to_num_list(line,' ') for line in block_data]

#data manipulation

def color_distance(color_1,color_2): 
    red_ajust=0.299
    green_ajust=0.587
    blue_ajust=0.114
    
    red_difference=(color_1[0]-color_2[0])**2
    green_difference=(color_1[1]-color_2[1])**2
    blue_difference=(color_1[2]-color_2[2])**2

    return (red_ajust*red_difference + green_ajust*green_difference + blue_ajust*blue_difference)**0.5
     
def get_block_info_by_RGB(color_data,block_data_list):
    rgb_values=text_to_num_list(color_data,',')
    
    start_block_rgb=[block_data_list[0][2],block_data_list[0][3],block_data_list[0][4]]
    mim_delta_E=color_distance(rgb_values,start_block_rgb)
    mim_delta_E_block=block_data_list[0]
   
    for block in block_data_list:
        block_rgb=[block[2],block[3],block[4]]
        delta_E=color_distance(rgb_values,block_rgb)
        if mim_delta_E>=delta_E:
            mim_delta_E=delta_E
            mim_delta_E_block=block
    return [mim_delta_E_block[0],mim_delta_E_block[1]]

def generate_lua_table(data):
    lua_table="data={"
    block_data_list=get_block_data()
    positions_indexs=[0,1,2]
    colors_indexs=[3,4,5]

    for line in data:
        line=line.strip('\n')
        line=line.split(',')
        
        position_data=get_line_data(line,positions_indexs)
        color_data=get_line_data(line,colors_indexs)
        block_info=get_block_info_by_RGB(color_data,block_data_list)

        table_line="{"+f"{position_data},{block_info[0]},{block_info[1]}"+'}'
        lua_table=lua_table+table_line+','               
    
    return lua_table.strip(',') +'}' 

def  main():  
    voxel_data=read_txt_file(data_path)
    lua_script_code=read_txt_file(base_code_path)
    lua_script_table=generate_lua_table(voxel_data)

    with open(lua_script_path,"w") as lua_script:
        lua_script.writelines(lua_script_table)
        lua_script.writelines(lua_script_code)
    
    print("Ready to go",end="")
    

if __name__=="__main__":
    main()

