# Import Dynamique
import os
import configparser
# Import Satatic
from lib.send import *
from lib.loc import *
import subprocess

# ini file config
config = configparser.ConfigParser()

def Error(i):
    if i == i:
        print("Probleme nommage erroner")
    return 0
def maximum(liste):
    ii = 0
    maxi = liste[0]
    for i in liste:
        if i >= maxi:
            maxi = i
            ii += 1
    return maxi

if __name__ == "__main__":
    cmd = 'ls -art ../ > allNameFile '
    os.system(cmd)
    print("##-------- Start Of The Process --------##")
    # Add All 'csv' file in 'tabCsv'
    # ------
    tabsCsv = []
    i = 0
    status = False
    # ---------
    fichier = open("allNameFile", "r")
    with fichier as filin:
        ligne = filin.readline()
        print("ligne = "+ligne)
        tabsCsv.append(ligne)
    fichier.close()

    if tabsCsv[0] == "":
        sendERRORmail()
        quit()
    else:
        # --- Send to ini file --
        put_in(tabsCsv)
    mainSend()
