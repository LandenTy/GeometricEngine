"""
demo

Description:
"""
# Modules
from Engine import *

# MATERIALS
c1 = Material((0,0,0))
c2 = Material((255,0,255))

# USERDEF
OBJ_FILE = "Cube.txt"
SAVE_FILE = "SavaData.txt"
MAT_LIST = [c1,c2]

OBJECT_NAME = "Cube_OBJ"

# Functions
obj_unpacker = Unpack_Obj()
obj_unpacker.unpack_obj_from_file(OBJ_FILE)
Save_Data(SAVE_FILE,obj_unpacker,OBJECT_NAME,MAT_LIST)
