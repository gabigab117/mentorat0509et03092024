import sys

"""
Le module sys en Python fournit des fonctionnalités liées à l'interpréteur Python et à son environnement. Il permet 
d'accéder à des variables et fonctions spécifiques au système, comme les arguments de ligne de commande, les chemins 
de recherche des modules, et le contrôle de l'entrée/sortie standard.
"""

# Exemple Django à montrer


def main():
    # Afficher les arguments de ligne de commande
    print("Arguments de ligne de commande :")
    print(sys.argv)
    for i, arg in enumerate(sys.argv):
        print(f"  Argument {i}: {arg}")

    # Afficher la version de Python
    print(f"\nVersion de Python : {sys.version}")

    # Afficher la plateforme
    print(f"Plateforme : {sys.platform}")

    # Afficher les chemins de recherche des modules
    # Script en cours, répertoires d'installation
    print("\nChemins de recherche des modules :")
    for path in sys.path:
        print(f"  {path}")

    # Exemple d'utilisation de sys.exit()
    if len(sys.argv) < 2:
        print("Erreur : Veuillez fournir au moins un argument.")
        sys.exit()

    print("\nLe script s'est exécuté avec succès.")


if __name__ == "__main__":
    main()
