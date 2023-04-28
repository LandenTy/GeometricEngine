"""
demo

Description:
"""
# Modules
from Engine import *

# MATERIALS
c1 = Material((0,124,124))

# USERDEF
OBJECT_NAME = ""
OBJ_FILE = ""
SAVE_FILE = ""
MAT_LIST = [c1]

# Functions
obj_unpacker = Unpack_Obj()
obj_unpacker.unpack_obj_from_file(OBJ_FILE)
Save_Data(SAVE_FILE,obj_unpacker,OBJECT_NAME,MAT_LIST)
