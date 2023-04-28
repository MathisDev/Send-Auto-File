import os
import configparser
# Import Satatic
from lib.send import *
from lib.loc import *

# ini file config
global config 
config = configparser.ConfigParser()

def trie(tab):
    tab_final = []
    status_usine = True
    status_base = True
    print(str(tab))
    for i in tab:
        if status_base == False and status_usine == False:
            if i[0:3] == 'base':
                if status_base == True:
                    tab_final.append(i)
                    status_base = False
            elif i[0:4] == 'Usine':
                if status_usine == True:
                    tab_final.append(i)
                    status_usine = False
            else:
                pass
        else:
            break
    return (tab_final)
            
def put_in(tabsCsv):
    print("tabCSV = "+str(tabsCsv))
    tab = trie(tabsCsv)
    config.read('config.ini')
    
    with open('config.ini', 'w') as configfile:
        config.write(configfile)