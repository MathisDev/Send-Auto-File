import os
import datetime


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
def main():
    # Add All 'csv' file in 'tabCsv'
    # ------
    tabsCsv = []
    i = 0
    # ---------
    with open("txt.txt", "r") as filin:
        ligne = filin.readline()
        while ligne != "":
            tabsCsv.append(ligne)
            ligne = filin.readline()
            i = i + 1

    print("----------")
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

    print(tabNbr)
    hightNbr = maximum(tabNbr)
    cout = 0

    while tabNbr[cout] != hightNbr:
        cout += 1
        print(cout)

    hightName = tabsCsv[cout]
    lenHightName = len(hightName) - 1
    hightName = hightName[0:lenHightName]
    print(hightName)
    os.system("mv "+hightName+" ftp/")
    #envoye Mail
    '''
    import smtplib,ssl
    mailFrom = ""
    mailDest = ""
    smtpMail = ""
    mailContent = '''

    '''
    from email.message import EmailMessage
    msg = EmailMessage()
    msg.set_content(mailContent)
    msg["Subject"] = "Fichier CSV"
    msg["From"] = mailFrom
    msg["To"] = mailDest
    context=ssl.create_default_context()
    with smtplib.SMTP(smtpMail, port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(msg["From"], "password")
        smtp.send_message(msg)
    '''
main() 