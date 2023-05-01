# Import Dynamique
import os
import configparser
import subprocess
# Import Satatic
from lib.send import *
# ini file config
config = configparser.ConfigParser()

def Error(i):
    if i == i:
        print("Probleme nommage erroner")
    return 0

if __name__ == "__main__":
    cmd = 'ls -d ../*Usine*.csv > allUsine && ls -d ../*base*.csv > allBase'
    os.system(cmd)
    print("##-------- Start Of The Process --------##")

    # ---- Create Dico -----
    dico_file = {}
    dico_file["base"] = 0
    dico_file["usine"] = 0

    # - Base -
    fichier_base = open("allBase", "r")
    line = fichier_base.readline()
    dico_file["base"] = line
    fichier_base.close()
    # - Usine -

    fichier_usine = open("allUsine", "r")
    line = fichier_usine.readline()
    dico_file["usine"] = line
    fichier_usine.close()

    if  dico_file["base"] == '' and dico_file["usine"] == '':
        sendERRORmail()
        quit()
    else:
       # --- Send to ini file --
        mainSend(dico_file)
        quit()
