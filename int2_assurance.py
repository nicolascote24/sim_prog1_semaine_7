# Initialisation des véhicules et de leurs primes de base
vehicules = ["Toyota Corolla", "Honda Civic", "Ford Focus", "Chevrolet Malibu", "Nissan Altima"]
primes_base = [1200, 1150, 1100, 1250, 1300]  # Correspond aux véhicules dans le même ordre

# Affichage des véhicules disponibles
print("Bienvenue dans le monde des assurances automobiles !")
print("Voici les véhicules que nous pouvons assurer :")
for i, vehicule in enumerate(vehicules):
    print(f"{i + 1}. {vehicule}")

# Demande à l'utilisateur de choisir un véhicule
choix_vehicule = int(input("Choisissez le numéro de votre véhicule : ")) - 1

# Vérification du choix
if choix_vehicule < 0 or choix_vehicule >= len(vehicules):
    print("Erreur : Choix de véhicule invalide.")
else:
    # Récupération de la prime de base
    prime_base = primes_base[choix_vehicule]
    print(f"Vous avez choisi : {vehicules[choix_vehicule]}")
    print(f"La prime de base pour ce véhicule est de : {prime_base} $")

    # Demande de l'âge du conducteur
    age_conducteur = int(input("Quel est votre âge ? "))
    
    # Calcul du supplément d'âge
    if age_conducteur < 17:
        print("Erreur : Vous devez avoir au moins 17 ans pour obtenir une assurance.")
    else:
        # Calcul du pourcentage d'âge
        pourcentage_age = 15 - (age_conducteur - 17)
        pourcentage_age = max(0, pourcentage_age)  # Ne pas descendre en dessous de 0%
        prime_age = prime_base * (pourcentage_age / 100)
        print(f"Supplément dû à l'âge : {prime_age:.2f} $")

        # Demande du kilométrage annuel
        kilometrage_annuel = int(input("Quel est votre kilométrage annuel ? "))
        ajout_km = (kilometrage_annuel // 500) * 8
        print(f"Montant supplémentaire dû au kilométrage : {ajout_km:.2f} $")

        # Demande des réclamations des 5 dernières années
        reclamations = []
        for i in range(5):
            montant_reclamation = float(input(f"Montant réclamé à l'assurance pour l'année {i + 1} (0 si aucune) : "))
            reclamations.append(montant_reclamation)

        # Calcul de la prime pour les réclamations
        ajout_reclamations = sum(3 for montant in reclamations if montant > 200)
        print(f"Montant supplémentaire dû aux réclamations : {ajout_reclamations:.2f} %")

        # Choix du type de couverture
        print("\nTypes de couverture disponibles :")
        print("1. De base : +0%")
        print("2. Des deux côtés : +10%")
        print("3. Totale : +15%")
        choix_couverture = int(input("Choisissez un type de couverture (1-3) : ")) - 1

        # Application du pourcentage en fonction de la couverture choisie
        pourcentage_couverture = [0, 10, 15]
        montant_couverture = (prime_base * pourcentage_couverture[choix_couverture] / 100)

        # Calcul final de la prime
        prime_totale = (prime_base + prime_age + ajout_km + ajout_reclamations + montant_couverture)
        print(f"\nLa prime d'assurance finale pour {vehicules[choix_vehicule]} est de : {prime_totale:.2f} $")