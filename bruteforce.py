import csv
import time

# Solution force brute - Recherche de toutes les solutions

# Cas d'un hear recursion (et non tail recursion). Les éléments produits par la recursivité
# sont stockés dans la stack memory en attendant d'être appelés.
# Udemy Recursion, Backtracking and Dynamic Programming in Python


combinaisons = []

def sacADos_force_brute(capacite, elements, elements_selection = []):
    # Utilisation d'une fonction récursive qui nécessite un point d'arrêt
    # Le pt d'arrêt est est-ce qu'il reste des éléments à traiter, oui, ou non (if elements)
    if elements:
        # si il y a toujours des éléments, on rappelle recursivement sacADos
        # dans 1 cas, on prend en considération l'objet courant (on le met ds le sac), pas dans l'autre cas
        val1, lstVal1 = sacADos_force_brute(capacite, elements[1:], elements_selection)
        # elements[1:] prend la liste moins le premier element, et lements_selection n'ajoute rien aux éléments elctionnés
        # if lstVal1 not in combinaisons:
        #     combinaisons.append(lstVal1)

        # ensuite on prend le premier élément de la liste d'éléments 
        val = elements[0]
        # et on vérifie que si on l'ajoute on est bien encore dans les limites de capacité du sac à dos
        if val[1] <= capacite:
            # si c'est ok, on rappelle la fonction en lui donnant la capacité moins le poids de l'objet (soit val[1])
            # on lui passe la liste privée du premier pour dire qu'il a été traité
            # on ajoute à élément_selection l'objet au complet (nom, poids, valeure) via val
            val2, lstVal2 = sacADos_force_brute(capacite - val[1], elements[1:], elements_selection + [val])
            # si val2 est plus favorable, on retourne val2 et listVal2 et inversement
            if val1 < val2:
                return val2, lstVal2

        return val1, lstVal1
    # si plus d'éléments dans la liste, on retourne le poids maxi et l'éléments sélectionné
    else:
        return round(sum([i[2] for i in elements_selection]),2), elements_selection

def result():
    print("combinaisons = ", combinaisons)
    print(len(combinaisons))

#----------------------------------------------
def main():
    start_time = time.time()
    # ele = [('Action-1', 20, 1), ('Action-2', 30, 3), ('Action-3', 50, 7.5), ('Action-4', 70, 14)]
    with open('datas/liste_actions.csv') as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=',')
        ele = []
        for ligne in reader:
            ele.append((ligne['name'], float(ligne['price']), round(float(ligne['price'])*(float(ligne['profit'])/100),2)))

    print(sacADos_force_brute(500, ele))
    # result()
    print("--- %s secondes ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()