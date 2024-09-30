# Initialisation des bataillons
bataillon_exploration = []
bataillon_garnison = []
bataillon_brigades_speciales = []

while True:
    print("\n=== Gestion des Bataillons ===")
    print("1. Ajouter un soldat")
    print("2. Transférer un soldat")
    print("3. Afficher les membres d'un bataillon")
    print("4. Afficher les membres de tous les bataillons")
    print("5. Quitter")

    choix = input("Choisissez une option : ")

    # Ajouter un soldat
    if choix == '1':
        nom_soldat = input("Entrez le nom du soldat : ")
        bataillon_choisi = input("Dans quel bataillon voulez-vous l'ajouter ? (exploration, garnison, brigades) : ").lower()

        # Vérification de l'ajout
        if bataillon_choisi == 'exploration':
            if len(bataillon_exploration) < 6:
                if nom_soldat not in bataillon_exploration:
                    bataillon_exploration.append(nom_soldat)
                    print(f"{nom_soldat} a été ajouté au bataillon d'exploration.")
                else:
                    print(f"Erreur : {nom_soldat} existe déjà dans le bataillon d'exploration.")
            else:
                print("Erreur : Le bataillon d'exploration est déjà plein.")
        
        elif bataillon_choisi == 'garnison':
            if len(bataillon_garnison) < 6:
                if nom_soldat not in bataillon_garnison:
                    bataillon_garnison.append(nom_soldat)
                    print(f"{nom_soldat} a été ajouté au bataillon de garnison.")
                else:
                    print(f"Erreur : {nom_soldat} existe déjà dans le bataillon de garnison.")
            else:
                print("Erreur : Le bataillon de garnison est déjà plein.")

        elif bataillon_choisi == 'brigades':
            if len(bataillon_brigades_speciales) < 6:
                if nom_soldat not in bataillon_brigades_speciales:
                    bataillon_brigades_speciales.append(nom_soldat)
                    print(f"{nom_soldat} a été ajouté au bataillon des brigades spéciales.")
                else:
                    print(f"Erreur : {nom_soldat} existe déjà dans le bataillon des brigades spéciales.")
            else:
                print("Erreur : Le bataillon des brigades spéciales est déjà plein.")
        
        else:
            print("Erreur : Bataillon invalide.")

    # Transférer un soldat
    elif choix == '2':
        nom_soldat = input("Entrez le nom du soldat à transférer : ")
        ancien_bataillon = input("De quel bataillon transférez-vous ce soldat ? (exploration, garnison, brigades) : ").lower()
        nouveau_bataillon = input("Dans quel bataillon souhaitez-vous le transférer ? (exploration, garnison, brigades) : ").lower()

        # Vérification du transfert
        if ancien_bataillon == 'exploration' and nom_soldat in bataillon_exploration:
            if nouveau_bataillon == 'garnison' and len(bataillon_garnison) < 6:
                bataillon_exploration.remove(nom_soldat)
                bataillon_garnison.append(nom_soldat)
                print(f"{nom_soldat} a été transféré du bataillon d'exploration au bataillon de garnison.")
            elif nouveau_bataillon == 'brigades' and len(bataillon_brigades_speciales) < 6:
                bataillon_exploration.remove(nom_soldat)
                bataillon_brigades_speciales.append(nom_soldat)
                print(f"{nom_soldat} a été transféré du bataillon d'exploration au bataillon des brigades spéciales.")
            else:
                print("Erreur : Le bataillon de destination est plein ou invalide.")
        
        elif ancien_bataillon == 'garnison' and nom_soldat in bataillon_garnison:
            if nouveau_bataillon == 'exploration' and len(bataillon_exploration) < 6:
                bataillon_garnison.remove(nom_soldat)
                bataillon_exploration.append(nom_soldat)
                print(f"{nom_soldat} a été transféré de la garnison au bataillon d'exploration.")
            elif nouveau_bataillon == 'brigades' and len(bataillon_brigades_speciales) < 6:
                bataillon_garnison.remove(nom_soldat)
                bataillon_brigades_speciales.append(nom_soldat)
                print(f"{nom_soldat} a été transféré de la garnison au bataillon des brigades spéciales.")
            else:
                print("Erreur : Le bataillon de destination est plein ou invalide.")
        
        elif ancien_bataillon == 'brigades' and nom_soldat in bataillon_brigades_speciales:
            if nouveau_bataillon == 'exploration' and len(bataillon_exploration) < 6:
                bataillon_brigades_speciales.remove(nom_soldat)
                bataillon_exploration.append(nom_soldat)
                print(f"{nom_soldat} a été transféré des brigades spéciales au bataillon d'exploration.")
            elif nouveau_bataillon == 'garnison' and len(bataillon_garnison) < 6:
                bataillon_brigades_speciales.remove(nom_soldat)
                bataillon_garnison.append(nom_soldat)
                print(f"{nom_soldat} a été transféré des brigades spéciales au bataillon de garnison.")
            else:
                print("Erreur : Le bataillon de destination est plein ou invalide.")
        
        else:
            print(f"Erreur : {nom_soldat} n'existe pas dans le bataillon {ancien_bataillon}.")

    # Afficher les membres d'un bataillon
    elif choix == '3':
        bataillon_choisi = input("Quel bataillon voulez-vous afficher ? (exploration, garnison, brigades) : ").lower()
        if bataillon_choisi == 'exploration':
            print("\nMembres du bataillon d'exploration :")
            if not bataillon_exploration:
                print("Aucun membre dans le bataillon d'exploration.")
            else:
                for soldat in bataillon_exploration:
                    print(f"- {soldat}")
        
        elif bataillon_choisi == 'garnison':
            print("\nMembres de la garnison :")
            if not bataillon_garnison:
                print("Aucun membre dans la garnison.")
            else:
                for soldat in bataillon_garnison:
                    print(f"- {soldat}")

        elif bataillon_choisi == 'brigades':
            print("\nMembres des brigades spéciales :")
            if not bataillon_brigades_speciales:
                print("Aucun membre dans les brigades spéciales.")
            else:
                for soldat in bataillon_brigades_speciales:
                    print(f"- {soldat}")

        else:
            print("Erreur : Bataillon invalide.")

    # Afficher tous les membres de tous les bataillons
    elif choix == '4':
        print("\n=== Membres de tous les bataillons ===")
        print("\nBataillon d'exploration :")
        for soldat in bataillon_exploration:
            print(f"- {soldat}")

        print("\nGarnison :")
        for soldat in bataillon_garnison:
            print(f"- {soldat}")

        print("\nBrigades spéciales :")
        for soldat in bataillon_brigades_speciales:
            print(f"- {soldat}")

    # Quitter le programme
    elif choix == '5':
        print("Au revoir !")
        break

    else:
        print("Erreur : Option invalide.")