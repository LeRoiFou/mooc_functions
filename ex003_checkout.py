
"""
Considérons les billets et pièces de valeurs suivantes : 20 euros, 10 euros, 5 euros, 2 euros et 1 euro. Écrire
une fonction rendre_monnaie qui reçoit en paramètre un entier prix et cinq valeurs entières x20, x10, x5, x2 et x1,
qui représentent le nombre de billets ou de pièces de chaque valeur que donne un client pour l’achat d’un objet dont
le prix est mentionné.
La fonction doit renvoyer cinq valeurs, représentant le nombre de billets et pièces de chaque sorte qu’il faut rendre
au client, dans le même ordre que précédemment. Cette décomposition doit être faite en rendant le plus possible de
billets et pièces de grosses valeurs.
Si la somme d’argent avancée par le client n’est pas suffisante pour effectuer l’achat, la fonction retournera cinq
valeurs None.

Éditeur : Laurent REYNAUD
Date : 21-07-2020
"""


# Fonction rendre_monnaie paramétrée qui comprend : l'argent à devoir et les versements effectués par le client
def rendre_monnaie(argent, res20, res10, res5, res2, res1):
    monnaie20 = res20 * 20
    monnaie10 = res10 * 10
    monnaie5 = res5 * 5
    monnaie2 = res2 * 2
    monnaie1 = res1 * 1
    verse = monnaie20+monnaie10+monnaie5+monnaie2+monnaie1
    solde = verse - argent
    if solde > 0:
        res20 = solde // 20
        solde = solde - res20*20
        res10 = solde // 10
        solde = solde - res10*10
        res5 = solde // 5
        solde = solde - res5*5
        res2 = solde // 2
        solde = solde - res2*2
        res1 = solde // 1
    elif solde == 0:
        res20 = 0
        res10 = 0
        res5 = 0
        res2 = 0
        res1 = 0
    else:
        res20 = None
        res10 = None
        res5 = None
        res2 = None
        res1 = None
    return res20, res10, res5, res2, res1


adevoir = int(input())
verse20 = int(input())
verse10 = int(input())
verse5 = int(input())
verse2 = int(input())
verse1 = int(input())

print(rendre_monnaie(adevoir, verse20, verse10, verse5, verse2, verse1))
