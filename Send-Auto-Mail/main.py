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
    subprocess.run(["bash", "../.bash.sh"])
    print("##-------- Start Of The Process --------##")
    # Add All 'csv' file in 'tabCsv'
    # ------
    tabsCsv = []
    i = 0
    status = False 
    # ---------
    fichier = open("allUsine.txt", "r")
    with fichier as filin:
        ligne = filin.readline()
        tabsCsv.append(ligne)
    fichier.close()
    fichier = open("allBase.txt", "r")
    with fichier as filin:
        ligne = filin.readline()
        tabsCsv.append(ligne)
    fichier.close()

    if tabsCsv[0] == "":
        sendERRORmail()
        quit()
    else:
        # --- Send to ini file -- 
        putINI(tabsCsv)
    mainSend()