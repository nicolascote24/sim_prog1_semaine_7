# Initialisation de la liste des joueurs
joueurs = ["Seong", "Choi", "Kang", "Oh", "Ali", "Jang"]

while True:
    print("\n=== Gestion des Joueurs de 'Squid Game' ===")
    print("1. Ajouter un joueur")
    print("2. Supprimer un joueur")
    print("3. Rechercher un joueur")
    print("4. Afficher la liste des joueurs")
    print("5. Quitter le programme")

    choix = input("Choisissez une option : ")

    # Ajouter un joueur
    if choix == '1':
        nom_joueur = input("Entrez le nom du joueur à ajouter : ")
        if nom_joueur in joueurs:
            print(f"Erreur : {nom_joueur} est déjà dans la liste.")
        else:
            joueurs.append(nom_joueur)
            print(f"{nom_joueur} a été ajouté à la liste.")

    # Supprimer un joueur
    elif choix == '2':
        nom_joueur = input("Entrez le nom du joueur à supprimer : ")
        if nom_joueur in joueurs:
            joueurs.remove(nom_joueur)
            print(f"{nom_joueur} a été supprimé de la liste.")
        else:
            print(f"Erreur : {nom_joueur} n'est pas dans la liste.")

    # Rechercher un joueur
    elif choix == '3':
        nom_joueur = input("Entrez le nom du joueur à rechercher : ")
        if nom_joueur in joueurs:
            indice = joueurs.index(nom_joueur)
            print(f"Le joueur {nom_joueur} est à l'indice {indice} dans la liste.")
        else:
            print(f"Erreur : {nom_joueur} n'existe pas dans la liste.")

    # Afficher la liste des joueurs
    elif choix == '4':
        print("\nListe des joueurs :")
        for index, joueur in enumerate(joueurs):
            print(f"{index}. {joueur}")

    # Quitter le programme
    elif choix == '5':
        print("Au revoir !")
        break

    else:
        print("Erreur : Option invalide.")