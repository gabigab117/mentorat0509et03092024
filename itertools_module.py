import itertools


# 1. repeat(): Répète un élément un nombre spécifié de fois
print(list(itertools.repeat('X', 4)))  # ['X', 'X', 'X', 'X']

# 2. combinations(): Génère toutes les combinaisons possibles
print(list(itertools.combinations('ABC', 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 3. permutations(): Génère toutes les permutations possibles
print(list(itertools.permutations('ABC', 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 4. chain(): Concatène plusieurs itérables
print(list(itertools.chain('ABC', '123')))  # ['A', 'B', 'C', '1', '2', '3']