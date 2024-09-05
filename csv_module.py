import csv  # Importe le module csv pour manipuler les fichiers CSV
from csv import DictWriter, DictReader

# Définit les données à écrire dans le fichier CSV
donnees = [
    ['Nom', 'Age', 'Ville'],  # En-têtes des colonnes
    ['Alice', '30', 'Paris'],  # Données de la première personne
    ['Bob', '25', 'Lyon'],    # Données de la deuxième personne
    ['Charlie', '35', 'Marseille']  # Données de la troisième personne
]

# Ouvre un nouveau fichier 'nouveau.csv' en mode écriture
with open('nouveau.csv', 'w') as fichier:
    ecrivain = csv.writer(fichier)  # Crée un objet writer pour écrire dans le fichier
    ecrivain.writerows(donnees)  # Écrit toutes les lignes de données d'un coup

# Lecture et affichage du fichier CSV en utilisant csv.reader
with open('nouveau.csv', 'r') as fichier:  # Ouvre le fichier en mode lecture
    lecteur = csv.reader(fichier)  # Crée un objet reader pour lire le fichier
    for ligne in lecteur:  # Parcourt chaque ligne du fichier
        print(ligne)  # Affiche chaque ligne sous forme de liste

# Lecture du fichier CSV en utilisant csv.DictReader pour un accès par nom de colonne
with open('nouveau.csv', 'r') as fichier:  # Ouvre à nouveau le fichier en mode lecture
    lecteur = csv.DictReader(fichier)  # Crée un objet DictReader
    # DictReader utilise automatiquement la première ligne comme en-têtes
    for ligne in lecteur:  # Parcourt chaque ligne du fichier
        # Affiche les données en accédant aux valeurs par le nom des colonnes
        print(f"Nom: {ligne['Nom']}, Age: {ligne['Age']}, Ville: {ligne['Ville']}")