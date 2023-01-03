import os
import configparser
from send import *

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
    print("##-------- Start Of The Process --------##")
    # Add All 'csv' file in 'tabCsv'
    # ------
    tabsCsv = []
    i = 0
    status = False 
    # ---------
    fichier1 = open("content.txt", "r")
    with fichier1 as filin:
        ligne = filin.readline()
        while ligne != "":
            tabsCsv.append(ligne)
            status = True
            ligne = filin.readline()
            i = i + 1
    fichier1.close()


    if status == False:
        hightName = "Error - Non '.csv' file "
        
    else:
        # Fin the laste
        # ------
        tailleListe = range(len(tabsCsv))
        tabNbr = []
        # ---------
        for tabCsv in tailleListe:
            nbr = ""
            name = tabsCsv[tabCsv]
            first = name[10]
            seg =  name[11]
            tird = name[12]
            # ------ 1
            if first.isnumeric():
                nbr = nbr + first
            else:
                Error(1)
            # ----- 2
            if seg.isnumeric():
                nbr = nbr + seg
            else:
                pass
            # ----- 3
            if tird.isnumeric():
                nbr = nbr + tird
            else:
                pass
            
            tabNbr.append(int(nbr))
            i += 1

        hightNbr = maximum(tabNbr)
        cout = 0

        while tabNbr[cout] != hightNbr:
            cout += 1

        hightName = tabsCsv[cout]
        lenHightName = len(hightName) - 1
        hightName = hightName[0:lenHightName]
    # --- Send to ini file
    config.read('config.ini')
    config.set('def','name',hightName)
    
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    
    mainSend()
