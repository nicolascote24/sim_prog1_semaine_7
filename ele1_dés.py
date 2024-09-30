import random
lst_lance = []

for x in range(1000):
    lst_lance.append(random.randint(1,6))
    
choix = int(input("voulez vous afficez tous les lancés (1) ou un lancé en particulier (2) : "))

if choix == 1:
    for x in lst_lance:
        print(f"résultat : {x}")
else:
    choix = int(input("inscrivez le numéro du lancer (de 0 à 999) : "))
    
    print(f"résultat : {lst_lance[choix]}")