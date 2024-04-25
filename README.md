## Description du Projet
Un script Python simple mais puissant pour le craquage de mots de passe en utilisant l'algorithme de hachage SHA-256. Ce script permet aux utilisateurs de vérifier si un hash SHA-256 donné correspond à un mot de passe dans un fichier spécifié. Il est principalement utilisé pour des fins éducatives et pour comprendre le fonctionnement du hachage SHA-256.

##Fonctionnalités
Hachage des mots de passe avec SHA-256.
Lecture de fichiers de mots de passe depuis le disque.
Affichage en temps réel des tentatives et comparaison avec le hash cible.
Possibilité de spécifier le fichier de mots de passe via la ligne de commande.

## Technologies Utilisées
Python 3
Bibliothèque hashlib pour le hachage
Bibliothèque pwn pour la gestion des logs

## Comment Commencer
Pour utiliser ce script, vous aurez besoin de Python installé sur votre système. Suivez les instructions ci-dessous pour configurer et exécuter le script :

###Clonage du projet:

Copy code
```git clone https://github.com/SdrSmith/SHA_Cracking.git```
Installation des dépendances (si nécessaire):
bash
Copy code
```cd SHA_Cracking```
```pip install -r requirements.txt```

Lancement du script:

Copy code
```python sha256_cracker.py <hash_sha256> <path_to_password_file>```

## Documentation
Le code est documenté pour expliquer chaque partie du processus de craquage. Des commentaires sont inclus pour clarifier les opérations clés.
