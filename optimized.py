import csv
import time



def sacADos_dynamique(invest_max, portfolio):
    matrice = [[0 for x in range(invest_max +1)] for x in range(len(portfolio) +1)]
    for share in range(1, len(portfolio) +1):
        for invest in range(1, invest_max +1):
            if portfolio[share-1][1] <= invest:
                matrice[share][invest] = max(portfolio[share-1][2] + matrice[share-1][invest-portfolio[share-1][1]], matrice[share-1][invest])
            else:
                matrice[share][invest] = matrice[share-1][invest]
    

    # Retrouver les élements en fonction de la somme
    investment = invest_max
    n = len(portfolio)
    shares_selection = []
    while investment >= 0 and n >= 0:
        e = portfolio[n-1]
        if matrice[n][investment] == matrice[n-1][investment-e[1]] + e[2]:
            shares_selection.append(e)
            # on diminue de l'investissement max, le prix de l'acion sélectionnée
            investment -= e[1]

        n -= 1

    return matrice[-1][-1], shares_selection

#----------------------------------------------
def main():
    start_time = time.time()

    ele = []
    with open('datas/dataset1.csv') as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=';')
        for ligne in reader:
            if float(ligne['price']) > 0 and float(ligne['profit']) > 0:
                price = float(ligne['price'])*100
                profit = float(ligne['profit'])
                profit_euros = (profit*price)/100
                ele.append((ligne['name'], int(price), profit_euros))
    
    result = sacADos_dynamique(50000, ele)

    print(result)
    print("")

    total_investment = 0
    for r in result[1]:
        total_investment += r[1]

    print(f"Investissement = {total_investment/100}, profit = {round((result[0]/100), 2)}")
    print("--- %s secondes ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()