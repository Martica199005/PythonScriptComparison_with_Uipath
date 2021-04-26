import sys
import os

#pip install fuzzywuzzy
#pip install fuzzywuzzy[speedup]
#pip install python-Levenshtein

import importlib

pyfilepath='your module path'
dirname, basename = os.path.split(pyfilepath) # pyfilepath: /my/path/mymodule.py
sys.path.append(dirname) # only directories should be added to PYTHONPATH
module_name = os.path.splitext(basename)[0] # /my/path/mymodule.py --> mymodule
module = importlib.import_module(module_name) # name space of defined module (otherwise we would literally look for "module_name")

print(module)


import fuzzywuzzy

from fuzzywuzzy import fuzz

def string_comparison(data,data1):
    try:
        return fuzz.ratio(data,data1)
    except:
        return "Error"


