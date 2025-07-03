def bonjour(nom):
    print(f"Bonjour,", nom, "!")

if __name__ == "__main__":
    user = input("Entrez votre nom : ")
    print("bonjour",user,",bienvenue! ")

def dire_aurevoir(nom):
    print(f"Au revoir, {nom} !")
if __name__ == "__main__":
    nom = input("Ton nom : ")
    dire_bonjour(nom)
    dire_aurevoir(nom)

