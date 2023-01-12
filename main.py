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
            nbr = ''
            name = tabsCsv[tabCsv]
            total = len(name)
            ii = 0 
            while ii != total:
                element = name[ii]
                if element.isnumeric():
                    nbr = nbr + element
                else:
                    pass
                ii = ii + 1
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
