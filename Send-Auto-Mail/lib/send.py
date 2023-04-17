## -- Import -- ##
import configparser
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def mailContent():
    fichier = open('contentMail/main_mail.txt','r')
    content = fichier.read()
    fichier.close()
    return content

def subjectContent():
    fichier = open('contentMail/sub_mail.txt','r')
    content = fichier.read()
    fichier.close()
    return content

def sendERRORmail(listeinfo):
    print('Error')

def sendMail(listeinfo,listedocs):
    mail_content = mailContent()
    subject = subjectContent()

    # define a docs to send
    usine_file = listedocs[0]
    usine_file = "../" + usine_file

    base_file = listedocs[1]
    base_file = "../" + base_file

    #The mail addresses and password
    receiver_address = listeinfo[0] # mail_1
    sender_pass = listeinfo[1]      # pass
    sender_address = listeinfo[2]   # mail_sender

    print("Login : "+sender_address)
    print('Pasword : '+sender_pass)
    print(" To ")
    print("recu par :"+receiver_address)

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject  #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    attachement_usine_file = open(usine_file, "rb")
    attachement_base_file = open(base_file, "rb")

    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p.set_payload((attachement_usine_file).read())
    
    # To change the payload into encoded form
    pa = MIMEBase('application', 'octet-stream')
    pa.set_payload((attachement_base_file).read())
    
    # encode into base64
    encoders.encode_base64(p)
    encoders.encode_base64(pa)
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % str("Usine CVS"))
    pa.add_header("Content-Dispodition", "attachement; filname=%s" % str("base CSV"))
    
    # attach the instance 'p' to instance 'msg'
    message.attach(p)
    message.attach(pa)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

def mainSend():
    # ini file config
    config = configparser.ConfigParser()
    config.read('config.ini')
    usine = config.get('def','usine') # Adress du dernier fichier usine
    base = config.get('def','base') # Adress du dernier fichier base
    
    retour = "Une erreur s'est produite lors de l'envoi de mail"

    # ini file info.ini

    config.read('info.ini')
    # Mail 
    mail_1 = config.get('info','mail_1')
    mail_2 = config.get('info','mail_2')
    mail_3 = config.get('info','mail_3')
    # Mail sender
    mail_sender = config.get('info','mail_sender')
    # Pass
    pasw = config.get('info','pass')

    listeOfMail = [mail_1,mail_2,mail_3]

    print("Sending ....")

    for x in listeOfMail:
        if x == "":
            pass
        else:
            listeInfo = [x,pasw,mail_sender]
            listeDoc = [usine,base]
            sendMail(listeInfo,listeDoc)

    print(" ##----- Send "+usine+ " and "+base+" ✅ -----##")