# Import Dynamique
import os
import os.path, time
import re
import configparser
import subprocess
from pathlib import Path
# Import Satatic
from lib.send import *


# ini file config
config = configparser.ConfigParser()


if __name__ == "__main__":
    path_liste = []
    dic_date = {}

    path = "../"
    dirs = os.listdir(path)
    dirs = sorted(dirs)
    csv_liste = []

    for dir in dirs:
        dir = "../" + dir
        path_liste.append(dir)

    for path_name in path_liste:
        dic_date[path_name] = time.ctime(os.path.getatime(path_name))

    dic_date = dict(sorted(dic_date.items(), key=lambda item:item[1],reverse=True))
    for el in dic_date:
        t_max = len(el)
        if el[t_max-4:t_max] == ".csv":
            csv_liste.append(el)
        else:
            pass

    # ---- Create Dico -----
    dico_file = {}
    dico_file["base"] = ""
    dico_file["usine"] = ""
    status_base = False
    status_usine = False
    for el in csv_liste:
        if el[19] == 'b':
            if status_base == False:
                dico_file["base"] = el
                status_base = True
            else:
                pass
        if el[26] == 'U':
            if status_usine == False:
                dico_file["usine"] = el
                status_usine == True
            else:
                pass

    if  (dico_file["base"] == "" and dico_file["base"] == "") and (dico_file["base"] == "" or dico_file["base"] == ""): 
        main_sendERRORmail()
    else:
       # --- Send to ini file --
        mainSend(dico_file)
        quit()