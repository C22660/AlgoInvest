import csv

# solution optimale (dynamique) (up down approche ?)

def sacADos_dynamique(invest_max, portfolio):
    matrice = [[0 for x in range(invest_max +1)] for x in range(len(portfolio) +1)]
    for i in range(1, len(portfolio) +1):
        for w in range(1, invest_max +1):
            if portfolio[i-1][1] <= w:
                # matrice[i][w] = max(portfolio[i-1][2] + matrice[i-1][int(w-portfolio[i-1][1])], matrice[i-1][w])
                matrice[i][w] = max(portfolio[i-1][2] + matrice[i-1][w-portfolio[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]
    

    # Retrouver les élements en fonction de la somme
    w = invest_max
    n = len(portfolio)
    shares_selection = []
    while w >= 0 and n >= 0:
        e = portfolio[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            shares_selection.append(e)
            w -= e[1]

        n -= 1

    return matrice[-1][-1], shares_selection

#----------------------------------------------
# ele = [('Action-1', 20, 1), ('Action-2', 30, 3), ('Action-3', 50, 7.5), ('Action-4', 70, 14), ('Action-5', 60, 10.2), ('Action-6', 80, 20), ('Action-7', 22, 1.54), ('Action-8', 26, 2.86), ('Action-9', 48, 6.24), ('Action-10', 34, 9.18), ('Action-11', 42, 7.14), ('Action-12', 110, 9.9), ('Action-13', 38, 8.74), ('Action-14', 14, 0.14), ('Action-15', 18, 0.54), ('Action-16', 8, 0.64), ('Action-17', 4, 0.48), ('Action-18', 10, 1.4), ('Action-19', 24, 5.04), ('Action-20', 114, 20.52)]
# ele_2 = [('Action-1', 20, 1), ('Action-2', 30, 3), ('Action-3', 50, 7.5), ('Action-4', 70, 14)]
ele = []
with open('datas/dataset1.csv') as fichier_csv:
   reader = csv.DictReader(fichier_csv, delimiter=';')
   for ligne in reader:
        if float(ligne['price']) > 0 and float(ligne['profit']) > 0:
            price = float(ligne['price'])
            profit = float(ligne['profit'])
            profit_euros = (profit*price)/100
            ele.append((ligne['name'], int(price), profit_euros))
       
result = sacADos_dynamique(500, ele)

print(result)
print("")

total_investment = 0
for r in result[1]:
    total_investment += r[1]

print(f"Investissement = {total_investment}, profit = {result[0]}")