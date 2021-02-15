"""
Le mot-clé 'def' annonce l'instruction d'une nouvelle fonction suivi du nom de la fonction (ici 'pgcd') Cette
fonction est paramétrée car entre les '()' figurent les variables qui vont être utilisées dans la fonction Par
principe, toute fonction dispose d'un bloc d'instruction (corps de fonction) qui se termine ici avec le mot-clé
'return' qui affichera le résultat

Éditeur : Laurent REYNAUD
Date : 20-07-2020
"""


def pgcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


# la fonction pgcd() est définie ci-après en tant que variable
le_pgcd = pgcd(112, 30)

print("PGCD de 112 et 30 vaut :", le_pgcd)
a = int(input("a = "))
if pgcd(a, 6) == 2:
    print("Le PGCD est égal à 2")
else:
    print("Le PGCD est différent de 2")

""" 
Fonction créée : pgcd() 
Fonctions prédéfinies : print(), int(), input() 
Mots-clés : def, while, return, if, else 
Variables : x,y,a  
"""
