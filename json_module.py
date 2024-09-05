import json

# Exemple de données Python
donnees = {
    "nom": "Dupont",
    "age": 30,
    "ville": "Paris",
    "interets": ["Python", "JSON", "Data Science"]
}

# dumps() : Convertit un objet Python en chaîne JSON
json_string = json.dumps(donnees, indent=2)
print("JSON string:")
print(json_string)
print(type(json_string))

# loads() : Convertit une chaîne JSON en objet Python
objet_python = json.loads(json_string)
print("\nObjet Python après loads():")
print(type(objet_python))
print(objet_python)
print(objet_python["nom"])
objet_python["nom"] = "Patrick"
print("\nObjet Python après loads() modifié:")
print(objet_python)

# dump() : Écrit un objet Python dans un fichier JSON
with open("donnees.json", "w") as fichier:
    json.dump(donnees, fichier, indent=2)
print("\nDonnées écrites dans 'donnees.json'")

# load() : Lit un fichier JSON et le convertit en objet Python
with open("donnees.json", "r") as fichier:
    donnees_lues = json.load(fichier)
print("\nDonnées lues depuis 'donnees.json':")
print(type(donnees_lues))
print(donnees_lues)


with open("nouvelles_donnees.json", "w") as fichier:
    donnees_lues["age"] = 40
    json.dump(donnees_lues, fichier, indent=2)