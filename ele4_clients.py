# Initialisation des listes pour chaque catégorie de risque
faible_risque = []
risque_modere = []
haut_risque = []

nb_client = int(input("entrez le nombre de clients : "))

# Demander à l'utilisateur d'entrer les informations pour 5 clients
for i in range(nb_client):
    nom_client = input(f"Entrez le nom du client {i + 1} : ")
    score_risque = int(input(f"Entrez le score de risque du client {nom_client} (0 à 100) : "))
    
    # Classification selon le score de risque
    if score_risque < 30:
        faible_risque.append(nom_client)
    elif 30 <= score_risque <= 70:
        risque_modere.append(nom_client)
    else:
        haut_risque.append(nom_client)

# Affichage des clients dans chaque catégorie
print("\n--- Classification des clients par risque ---")
print(f"Clients à faible risque : {faible_risque}")
print(f"Clients à risque modéré : {risque_modere}")
print(f"Clients à haut risque : {haut_risque}")