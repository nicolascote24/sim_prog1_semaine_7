primes = [100, 110, 120, 130, 110, 100, 90, 95, 105, 115, 125, 135] #primes de bases
mois = ["janvier", "fevrier", "mars","avril", "mai", "juin","juillet", "aout", "septembre","octobre", "novembre", "decembre"] #liste des mois 
primes_finales = [] #liste vide pour les primes finales du client

age = int(input("Entrez l'âge du client : "))

# Ajustement des primes en fonction de l'âge
if age < 30:
    primes_finales = primes
elif 30 <= age <= 60:
    primes_finales = [prime * 1.10 for prime in primes]
else:
    primes_finales = [prime * 1.20 for prime in primes]

# Calcul du total annuel
for x in range(12):
    print(f"prime du mois de {mois[x]} : {int(primes_finales[x])}")