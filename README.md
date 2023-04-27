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

-- Installation -- 

Avoir Python 3.10 . link:https://www.python.org/downloads/
Compiler avec pyinstaller le main.py en onefile . link:https://wiki-fablab.grandbesancon.fr/doku.php?id=howto:python:pyinstaller
Remplacer le main.exe a la pace de l'ancien main puis suprimer tout dossier ou ficher superflue du a la compilation .
Puis ajouter le .exe a une tache tout les mois .

Win+R and typing 'taskschd.msc'
If you don’t have administrative permission, you have to hit Win+R and type 'runas /user:${ADMIN}' taskschd.msc 
 - Create a basic task
 - Monthly
Script :
Path of the sendAutoFile make


