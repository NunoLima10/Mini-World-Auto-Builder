
import struct

from collections import namedtuple
from pallete import  Pallete
from Exceptions import VoxHasNoPalleteException,VoxPaserException,FileNotFoundException


Voxel = namedtuple("Voxel", "x y z c")
Size = namedtuple("Size", "x y z")
Color = namedtuple("Color", "r g b a")


class VoxParser:
    def __init__(self, path: str) -> None:
        self.path = path
        self.use_palette = True

        self.version: str = None
        self.size: tuple = None
        self.voxels = []
        self.palette = []

    def import_vox(self, pallete: Pallete, load_frame=0) -> None:
            

            with open(self.path, 'rb') as vox:
                current_frame = 0

                if not struct.unpack('<4c', vox.read(4)) == (b'V', b'O', b'X', b' '):
                      raise VoxPaserException("Voxel format not supported")

                self.version = struct.unpack('<i', vox.read(4))

                if not struct.unpack('<4c', vox.read(4)) == (b'M', b'A', b'I', b'N'):
                    raise VoxPaserException("Voxel format not supported")
                
                N, M = struct.unpack('<ii', vox.read(8))
                if N != 0:
                    raise VoxPaserException("Voxel format not supported")

                while True:
                    try:
                        *name, s_self, s_child = struct.unpack('<4cii', vox.read(12))
                        if s_child != 0:
                            raise VoxPaserException("Voxel format not supported")

                        name = b''.join(name).decode('utf-8') 

                    except struct.error:
                        # end of file
                        break
                    if name == 'PACK':
                        # number of models
                        num_models, = struct.unpack('<i', vox.read(4))

                        # clamp load_frame to total number of frames
                        load_frame = min(load_frame, num_models)
                    elif name == 'SIZE':
                        # model size
                        x, y, z = struct.unpack('<3i', vox.read(12))
                        self.size = Size(x, y, z)
                        
                    elif name == 'nTRN':
                        break
                    elif name == 'XYZI':
                        # voxel data
                        if current_frame == load_frame:
                            num_voxels, = struct.unpack('<i', vox.read(4))
                            for voxel in range(num_voxels):
                                voxel_data = struct.unpack('<4B', vox.read(4))
                                x, y, z, c = voxel_data
                                self.voxels.append(Voxel(x, y, z, c))
                        else:
                            print("Skipping voxels in frame #{}".format(current_frame))
                            vox.read(s_self)
                        current_frame += 1
                    elif name == 'RGBA':
                        # palette
                        for col in range(256):
                            color_data = struct.unpack('<4B', vox.read(4))
                            r, g, b, a = color_data
                            #self.palette.append(Color(r, g, b, a))
                    elif name == 'MATT':
                        pass
                    else:
                        # Any other chunk, we don't know how to handle
                        raise VoxPaserException("Voxel format not supported")
                        
            if not self.palette: 
                try:
                    pallete.load()
                    for pixel in pallete.pixels:
                        r, g, b, a =  pixel
                        self.palette.append(Color(r, g, b, a))
                except FileNotFoundException:
                    raise VoxHasNoPalleteException
               

                
       



        

        