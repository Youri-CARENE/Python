Mettre à jour le système:
Ouvrez un terminal et exécutez la commande suivante pour mettre à jour la liste des paquets et installer les mises à jour disponibles :

 
sudo apt update && sudo apt upgrade -y
Installer les dépendances:
Installez les paquets nécessaires pour ajouter un nouveau dépôt avec la commande suivante :

 
sudo apt install -y software-properties-common
Ajouter le dépôt "deadsnakes" PPA:
Le PPA "deadsnakes" contient plusieurs versions de Python, y compris Python 3.8. Ajoutez le PPA avec la commande suivante :

 
sudo add-apt-repository ppa:deadsnakes/ppa
Confirmez l'ajout du dépôt en appuyant sur "Enter".

Installer Python 3.8:
Mettez à jour la liste des paquets et installez Python 3.8 avec la commande suivante :

 
sudo apt update && sudo apt install -y python3.8
Vérifier l'installation:
Vérifiez que Python 3.8 est installé en exécutant la commande suivante :

 
python3.8 --version
Si l'installation a réussi, la version de Python 3.8 sera affichée.

Installer pip pour Python 3.8 (optionnel) :
Si vous souhaitez installer pip pour gérer les paquets Python pour Python 3.8, exécutez la commande suivante :

 
sudo apt install -y python3.8-venv python3.8-dev
wget https://bootstrap.pypa.io/get-pip.py
python3.8 get-pip.py
Cela installera pip pour Python 3.8 et vous pourrez l'utiliser avec la commande pip3.8.