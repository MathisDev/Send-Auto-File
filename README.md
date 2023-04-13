# Send-Auto-File

Détection et envoie par mail du fichier le plus recent dans le dossier cible (csVfile) .

L'app Contient plusieurs elements :

- makefile . permet de lancer l'ensemble du programme .
- bash.sh . Copie des fichiers csv dans le fichier content.txt .
- main.py . Fichier Python3.10 qui a en sortie le fichier csv avec l'indice le plus grand exemple comptage1.csv < comptage5.csv .
- send.py . Fichier Python3.10 qui envoie par mail le fichier comptage déterminer comme ayant l'indice le plus grand par le fichier main.py .
- Les fichiers csv .

Fichier de configuration :
- info.ini . Contient les informations nécessaires à l'envoi de mail .
  Trois adresses mails sont disponibles pour les adresses de destinations .
  L’ adresse mail d’envoi est a créer et a definire dans info.ini .
- config.ini . Stockage par le programme du nom du fichier Csv (le fichier a envoyer) avec l'indice le plus grand .

L'ensemble de l'application doit être installé pour que le dossier cible de réception des fichiers .csv soit le csVfile .
L'automatisation du lancement du processus est géré grace a CRON tous les premiers du mois .



-- Planification -- 

Include dans le fichier d'installation
Sinon :

Win+R and typing 'taskschd.msc'
If you don’t have administrative permission, you have to hit Win+R and type 'runas /user:${ADMIN}' taskschd.msc 
 - Create a basic task
 - Monthly
Script :
Path of the sendAutoFile make


