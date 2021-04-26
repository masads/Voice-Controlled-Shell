import os
from ctypes import *

lib = cdll.LoadLibrary('./example.so')
lib.return_string.restype = c_char_p
lib.return_string.argtypes = [c_char_p]
name = create_string_buffer("Tom")
s = lib.return_string(name)
print (s)
print (name)