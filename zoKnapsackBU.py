import csv
# bottom up approche
def zoKnapsackBU(profits, prices, invest_max):
    if invest_max <= 0 or len(profits) == 0 or len(prices) != len(profits):
        return 0
    numberOfRows = len(profits) + 1
    dp = [[0 for i in range(invest_max+2)] for j in range(numberOfRows)]
    for row in range(numberOfRows-2, -1, -1):
        for column in range(1, invest_max+1):
            profit1 = 0
            profit2 = 0
            if prices[row] <= column:
                profit1 = profits[row] + dp[row + 1][column - prices[row]]
            profit2 = dp[row +1][column]
            dp[row][column] = max(profit1, profit2)
    return dp[0][invest_max]

# ele = [('Action-1', 20, 1), ('Action-2', 30, 3), ('Action-3', 50, 7.5), ('Action-4', 70, 14)]
# with open('datas/liste_actions.csv') as fichier_csv:
#    reader = csv.DictReader(fichier_csv, delimiter=',')
#    profits = []
#    prices = []
#    for ligne in reader:
#         profits.append(round(float(ligne['price'])*(float(ligne['profit'])/100),2))
#         prices.append(float(ligne['price']))

profits = []
prices = []
with open('datas/dataset1.csv') as fichier_csv:
   reader = csv.DictReader(fichier_csv, delimiter=';')
   for ligne in reader:
        if float(ligne['price']) >= 0 and float(ligne['profit']) >= 0:
            # price = int(float(ligne['price'])*100)
            # profit = int(float(ligne['profit']))
            # profit_euros = int((profit*price)/100)
            # profits.append(profit_euros)
            # prices.append(price)
            price = float(ligne['price'])
            profit = float(ligne['profit'])
            profit_euros = (profit*price)/100
            profits.append(profit_euros)
            prices.append(int(price)) # conversion en Int car va servir d'index

print(zoKnapsackBU(profits, prices, 500))