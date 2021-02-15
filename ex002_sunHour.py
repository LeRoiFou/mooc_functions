"""
Dans un premier temps écrire une fonction soleil_leve qui, pour un soleil particulier, reçoit trois valeurs
entières en argument pour la planète : - l'heure de lever du soleil (entre 0 et 23) - l'heure du coucher du soleil (
entre 0 et 23) - l'heure actuelle (entre 0 et 23) et qui renvoie une valeur booléenne vraie si le soleil est levé sur
la planète à l'heure donnée en troisième argument et fausse, s'il est couché.

On supposera que chacun des soleils ne se lève et ne se couche au plus qu'une seule fois par jour. Il est toutefois
possible que le lever ait lieu après l'heure du coucher, ce qui signifie dans ce cas que le soleil est levé au début
de la journée, puis qu'il se couche, puis qu'il se lève à nouveau plus tard dans la journée. Enfin, si l'heure du
lever est la même que l'heure du coucher : - soit toutes deux valent 12, cela signifie que le soleil ne se lève pas
de la journée, - soit toutes les deux valent 0, cela signifie que le soleil ne se couche pas de la journée.

Éditeur : Laurent REYNAUD
Date : 20-07-2020
"""


def soleil_leve(heure_leve, heure_coucher, heure_actuelle):
    cas1 = heure_leve == heure_coucher == 0
    cas2 = heure_leve == heure_coucher == 12
    cas3 = heure_leve != heure_coucher
    cas4 = heure_leve <= heure_actuelle < heure_coucher
    cas5 = heure_actuelle < heure_coucher <= heure_leve
    cas6 = heure_coucher < heure_leve <= heure_actuelle
    if cas1:
        return True
    elif cas2:
        return False
    elif cas3:
        if cas4 or cas5 or cas6:
            return True
        else:
            return False


x = int(input())
y = int(input())
z = int(input())

print(soleil_leve(x, y, z))
