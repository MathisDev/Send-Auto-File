# Send-Auto-File

Détection et envoie par mail du fichier le plus recent dans le dossier cible (csVfile) .

L'app Contient plusieurs elements :

- bash.sh . Copie des fichiers csv dans le fichier content.txt .
- main.py . Fichier Python3.10 qui a en sortie les dernier fichier csv usine est base soit definit .
- send.py . Fichier Python3.10 qui envoie par mail le fichier comptage déterminer par le fichier main.py .
- Les fichiers csv .

Fichier de configuration :
- config.ini . Stockage par le programme du nom du fichier Csv (le fichier a envoyer) avec l'indice le plus grand .
- allBase.txt et allUsine.txt son des fichier systeme .

Votre Configuration :
- info.ini . Contient les informations nécessaires pour l'envoi de mail , Vous pouvez definir jusqu'a trois adresses mails de destinations .
- contentMail/main_mail.txt . Pour définir le message principal du mail . 
- contentMail/sub_mail.txt . Pour définir le sujet du mail . 

-- Planification -- 

Include dans le fichier d'installation
Sinon :

Win+R and typing 'taskschd.msc'
If you don’t have administrative permission, you have to hit Win+R and type 'runas /user:${ADMIN}' taskschd.msc 
 - Create a basic task
 - Monthly
Script :
Path of the sendAutoFile make


