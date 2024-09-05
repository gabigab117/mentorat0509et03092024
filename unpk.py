# Le déballage en Python avec l'opérateur *

# 1. Déballage d'une liste ou d'un tuple
print("1. Déballage d'une liste ou d'un tuple")
a, *b, c, d = (1, 2, 3, 4, 5)
print(f"a = {a}, b = {b}, c = {c}, d = {d}")
print(type(b))

print("_" * 40)

# 2. Fusion de listes
print("2. Fusion de listes")
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste_fusionnee = [*liste1, *liste2]
print(f"Liste fusionnée : {liste_fusionnee}")
# Résultat : Liste fusionnée : [1, 2, 3, 4, 5, 6]

print("_" * 40)

# 3. Déballage dans les appels de fonction
print("3. Déballage dans les appels de fonction")
def somme(a, b, c):
    return a + b + c

nombres = [1, 2, 3]
resultat = somme(*nombres)
print(f"Somme : {resultat}")
# Résultat : Somme : 6

print("_" * 40)

# 4. Collecte d'arguments restants dans une fonction
print("4. Collecte d'arguments restants dans une fonction")
def fonction(premier, *args):
    print(f"Premier argument : {premier}")
    print(f"Arguments restants : {args}")

fonction(1, 2, 3, 4, 5, "Ma Chaine")
# Résultat :
# Premier argument : 1
# Arguments restants : (2, 3, 4, 5)

print("_" * 40)

# 5. Déballage de dictionnaires avec **
print("5. Déballage de dictionnaires avec **")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict_fusionne = {**dict1, **dict2}
print(f"Dictionnaire fusionné : {dict_fusionne}")
# Résultat : Dictionnaire fusionné : {'a': 1, 'b': 2, 'c': 3, 'd': 4}