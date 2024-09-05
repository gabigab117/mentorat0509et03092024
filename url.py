import urllib.parse
import urllib.request
import urllib.error

# url standard pour travailler avec les urls

def open_and_read_url():
    print("1. Ouvrir une URL et lire son contenu:")
    url = "https://www.docstring.fr/"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(html[:500])  # Affiche les 500 premiers caractères


def parse_url():
    print("\n2. Analyser une URL:")
    url = "https://www.example.com/path?param=value"
    parsed_url = urllib.parse.urlparse(url)
    print(f"Scheme: {parsed_url.scheme}")
    print(f"Netloc: {parsed_url.netloc}")


def download_file():
    print("\n4. Télécharger un fichier:")
    url = "https://onsenbray.fr/wp-content/uploads/2023/10/cropped-cropped-ons2-scaled-1-1.jpg"
    try:
        filename, headers = urllib.request.urlretrieve(url, "img.jpg") # url du fichier à dl
        print(f"Fichier téléchargé: {filename} - {headers}")
    except urllib.error.URLError:
        print("Erreur lors du téléchargement")
