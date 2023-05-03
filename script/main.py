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
    print("Start of the process")
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

    for el in csv_liste:
        if el[19] == 'b':
            if dico_file["base"] == "":
                dico_file["base"] = el
            else:
                pass
        if el[26] == 'U':
            if dico_file["usine"] == "":
                dico_file["usine"] = el
            else:
                pass

    if  (dico_file["base"] == "" and dico_file["usine"] == "") or (dico_file["base"] == "" or dico_file["base"] == ""):
        pass
    else:
       # --- Send to ini file --
        mainSend(dico_file)
