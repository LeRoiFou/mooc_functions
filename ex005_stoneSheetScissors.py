"""
Cet exercice et le suivant vous demandent de programmer le petit jeu appelé « Pierre-feuille-ciseaux » ou «
Pierre-papier-ciseaux » (et qui porte encore d’autres noms comme indiqué dans la page Pierre-papier-ciseaux sur
Wikipedia que nous utilisons pour rédiger l’énoncé ci-dessous).

Pierre-feuille-ciseaux est un jeu effectué avec les mains et opposant un ou plusieurs joueurs. Ici nous nous
supposerons qu’il y a deux joueurs : l’ordinateur et le joueur lui-même.

Déroulement du jeu Les deux joueurs choisissent simultanément un des trois coups possibles en le symbolisant de la
main :
-> poing fermé : Pierre ;
-> main ouverte, doigts collés les uns aux autres : Feuille ;
-> main avec pouce, annulaire et auriculaire fermé, index et majeur ouvert en forme de V : Ciseaux.

Résultat du jeu :
-> la pierre bat les ciseaux (en les émoussant),
-> les ciseaux battent la feuille (en la coupant),
-> la feuille bat la pierre (en l’enveloppant).
Ainsi chaque coup bat un autre coup, fait match nul contre le deuxième (son homologue) et est battu par le troisième.

Écrire une fonction bat( joueur_1, joueur_2) où joueur_1 et joueur_2 ont chacun une valeur entière 0, 1 ou 2,
qui encode ce que le joueur a fait comme coup (0 : PIERRE, 1 : FEUILLE, 2 : CISEAUX) qui renvoie un résultat booléen :
vrai si joueur_1 bat le joueur_2 :
faux si joueur_2 bat joueur_1 ou fait match nul contre lui.


Éditeur : Laurent REYNAUD
Date : 22-07-2020
"""


def bat(joueur_1, joueur_2):
    if joueur_1 == 0 and joueur_2 == 2:
        return True
    elif joueur_1 == 1 and joueur_2 == 0:
        return True
    elif joueur_1 == 2 and joueur_2 == 1:
        return True
    else:
        return False


j1 = int(input())
j2 = int(input())
print(bat(j1, j2))
