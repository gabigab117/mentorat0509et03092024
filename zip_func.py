# La fonction zip() en Python
## Itérables, donne un itérateur
# Parcourir les listes en parallèle, créer des dictionnaires
## En cas de longueur différente; zip s'arrête lorsque le plus court est épuisé.

# Exemple 1 : Combinaison basique de deux listes
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for nom, age in zip(noms, ages):
    print(f"{nom} a {age} ans.")


print("_" * 40)

# Exemple 2 : Création d'un dictionnaire
cles = ["a", "b", "c"]
valeurs = [1, 2, 3]

mon_dict = dict(zip(cles, valeurs))
print(mon_dict)  # {'a': 1, 'b': 2, 'c': 3}

print("_" * 40)

# Exemple 3 : Utilisation avec des itérables de longueurs différentes
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c"]

for num, lettre in zip(list1, list2):
    print(f"{num} - {lettre}")


print("_" * 40)

# Exemple 4 : Utilisation de zip() avec plus de deux itérables
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = [True, False, True]

for num, lettre, booleen in zip(list1, list2, list3):
    print(f"{num} - {lettre} - {booleen}")


print("_" * 40)

# Exemple 5 : Déballage d'une liste de tuples
pairs = [(1, "un"), (2, "deux"), (3, "trois")]
nombres, mots = zip(*pairs)

print(nombres)  # (1, 2, 3)
print(mots)     # ('un', 'deux', 'trois')