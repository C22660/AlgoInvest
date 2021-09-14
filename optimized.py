import csv
import time

""" Scripte optimisé pour maximiser les profits sur les fichiers dataset1
et dataset2
"""


def sac_a_dos_dynamique(invest_max, portfolio):
    """A partir d'une matrice, va déterminer la meilleure option d'invetissement

    Args:
        invest_max (int): Investissement max multiplié par 100 pur éviter les virgules
        portfolio (list): Ensemble des actions avec nom, prix et profit

    Returns:
        [float, list]: le profit total et la liste des actions retenues
    """
    matrice = [[0 for x in range(invest_max + 1)] for x in range(len(portfolio) + 1)]
    for share in range(1, len(portfolio) + 1):
        for invest in range(1, invest_max + 1):
            if portfolio[share-1][1] <= invest:
                matrice[share][invest] = max(portfolio[share-1][2] + matrice[share-1]
                                             [invest-portfolio[share-1][1]],
                                             matrice[share-1][invest])
            else:
                matrice[share][invest] = matrice[share-1][invest]

    # Retrouver les élements en fonction de la somme
    investment = invest_max
    n = len(portfolio)
    shares_selection = []
    while investment >= 0 and n >= 0:
        e = portfolio[n-1]
        if matrice[n][investment] == matrice[n-1][investment-e[1]] + e[2]:
            # shares_selection.append(e)
            shares_selection.append((e[0], e[1]/100, round((e[2]/100), 2)))
            # on diminue de l'investissement max, le prix de l'acion sélectionnée
            investment -= e[1]

        n -= 1

    return round((matrice[-1][-1]/100), 2), shares_selection


# ----------------------------------------------
def main():
    choix = input("Quel fichier voulez vous optimiser ? \n \
        Saisissez 1 pour dataset1, 2 pour dataset2 ")
    if choix == "1":
        data = 'datas/dataset1.csv'
        limiter = ';'
    elif choix == "2":
        data = 'datas/dataset2.csv'
        limiter = ','
        start_time = time.time()
    else:
        print("")
        print("Désolé, seules les réponses 1 ou 2 sont possibles.")
        exit()

    start_time = time.time()
    ele = []
    with open(data) as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=limiter)
        for ligne in reader:
            if float(ligne['price']) > 0 and float(ligne['profit']) > 0:
                price = float(ligne['price'])*100
                profit = float(ligne['profit'])
                profit_euros = (profit*price)/100
                ele.append((ligne['name'], int(price), profit_euros))

    result = sac_a_dos_dynamique(50000, ele)

    print(result)
    print("")

    total_investment = 0
    for r in result[1]:
        total_investment += r[1]

    print(f"Investissement = {total_investment},"
          f" profit = {result[0]}")
    print("--- %s secondes ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
