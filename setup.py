
from distutils.core import setup
from distutils.core import Extension
MOD= "rcmd"
module = Extension(MOD, sources =["run_cmd_file.c"])
setup(name = MOD,
		ext_modules = [module])
