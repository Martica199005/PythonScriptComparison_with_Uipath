# PythonScriptComparison_with_Uipath
 Install the following libraries with pip command:
pip install fuzzywuzzy
pip install fuzzywuzzy[speedup]
pip install python-Levenshtein

Due to a Uipath limitation, Python activity uses, by default, the installation location of the Python activities pack as the run directory for the script. To change this, and to be able to use relative paths inside the script, you can add the following code to the loaded script as a workaround:

import sys 
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import <your module here>
  
  I've simplified it in the script in the following way:
  
import importlib

pyfilepath='your module path'  # replace \ with \\ , example 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\fuzzywuzzy'
dirname, basename = os.path.split(pyfilepath) # pyfilepath: /my/path/mymodule.py
sys.path.append(dirname) # only directories should be added to PYTHONPATH
module_name = os.path.splitext(basename)[0] # /my/path/mymodule.py --> mymodule
module = importlib.import_module(module_name)

print(module) #if you print the module in this case it will be fuzzywuzzy
