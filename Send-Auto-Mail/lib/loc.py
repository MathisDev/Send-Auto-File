import os
import configparser
# Import Satatic
from lib.send import *
from lib.loc import *

# ini file config
global config 
config = configparser.ConfigParser()

def putINI(tabsCsv):
    config.read('config.ini')
    config.set('def','usine',tabsCsv[0])
    config.set('def','base',tabsCsv[1])
    
    with open('config.ini', 'w') as configfile:
        config.write(configfile)