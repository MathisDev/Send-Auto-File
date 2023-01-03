## -- Import -- ##
import configparser
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def mailContent():
    fichier = open('content/main_mail.txt','r')
    content = fichier.read()
    fichier.close()
    return content

def subjectContent():
    fichier = open('content/sub_mail.txt','r')
    content = fichier.read()
    fichier.close()
    return content

def sendERRORmail(listeinfo):
    print('Error')

def sendMail(listeinfo):
    mail_content = mailContent()
    subject = subjectContent()
    #The mail addresses and password
    file = listeinfo[0]
    file = "csVfile/" + file 
    receiver_address = listeinfo[1] # mail_1
    sender_pass = listeinfo[2]      # pass
    sender_address = listeinfo[3]   # mail_sender

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

    attachement = open(file, "rb")

    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p.set_payload((attachement).read())
    
    # encode into base64
    encoders.encode_base64(p)
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % file)
    
    # attach the instance 'p' to instance 'msg'
    message.attach(p)
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
    file = config.get('def','name') # Adress du fichier le plus grand
    
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

    try:
        for x in listeOfMail:
            if x == "":
                pass
            else:
                listeInfo = [file,x,pasw,mail_sender]
                sendMail(listeInfo)

    except:
        for x in listeOfMail:
            if x == "":
                pass
            else:
                listeInfo = [file,x,pasw,mail_sender] 
                sendMail(listeInfo)

    print(" ##----- Send "+file+" ✅ -----##")