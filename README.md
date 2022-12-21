# SendLargesteFileFTP
L'app Contient plusieur element :

- makefile . Qui permet de lancer l'ensemble du programme .
- bash.sh . Copie des fichier csv dans le fichier content.txt .
- main.py . Fichier Python3.10 qui detecte et a en sortie le fichier csv avec l'indice le plus grand exemple comptage1.csv < comptage5.csv .
- send.py . Fichier Python3.10 qui envoie par mail le fichier compatage determiner comme aillant l'indice le plus grand par le fichier main.py .
- Les fichier csv .

L'ensemble de l'application doit etre intaller dans le ficher cible de reception des fichiers .csv
L'automatisation du lancement du processus est géré grace a cron tout les premier du mois .

Detection et envoye par mail du fichier le plus recent sur un depot FTP .
