import time
import csv


def binary_code_chart(elements, invest_max):
    chart_combinations = []
    number_of_combinations = 2 ** len(elements)
    valid_combinations = []  # car respecte la limite d'investissement

    for i in range(0, number_of_combinations):
        binary_code = bin(i)[2:]
        complete_code = '0'*(len(elements)-len(binary_code))+binary_code
        # pour 3 actions : ['000', '001', '010', '011', '100', '101', '110', '111']
        chart_combinations.append(complete_code)
    # Parcourir les combinaisons
    for combination in chart_combinations:
        cumul_price = 0
        for index, value in enumerate(combination):
            if value == str(1):
                cumul_price += elements[index][1]
        # si le cumul des prix des actions associées ne dépasse pas inves max,
        # alors prise en compte
        if cumul_price <= invest_max and cumul_price > 0:
            valid_combinations.append(combination)

    # pour 3 actions : ['001', '010', '011', '100']
    return valid_combinations


# une fois la liste des combinaisons possibles est établie :
# - Calcul du prix de la combinaisons
def combination_invest(selection):
    total_price = 0
    for prices in selection:
        total_price += prices[1]
    return total_price


# - Calcul du profit de la combinaisons
def combination_profit(selection):
    total_profit = 0
    for profits in selection:
        total_profit += profits[2]
    return total_profit


# Optimisation de la selection

def best_combination(combinations):
    best_profit = 0
    total_invest = 0
    best_solution = []
    for combination in combinations:
        invest = combination_invest(combination)
        profit = combination_profit(combination)
        if profit > best_profit:
            best_profit = profit
            total_invest = invest
            best_solution = combination

    return best_profit, total_invest, best_solution

# # fonction force brute :


def portfolio_analysis(elements, invest_max):
    options = []
    chart = binary_code_chart(elements, invest_max)
    # Traduction des combinaisons possible binaire en éléments
    for code in chart:
        option = []
        for index, value in enumerate(code):
            if value == str(1):
                option.append(elements[index])
        options.append(option)

    solution = best_combination(options)

    return solution

# ----------------------------------------------


def main():
    start_time = time.time()
    # ele_2 = [('Action-1', 4, 12), ('Action-2', 3, 10), ('Action-3', 2, 6)]
    with open('datas/liste_actions.csv') as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=',')
        ele = []
        for ligne in reader:
            ele.append((ligne['name'], float(ligne['price']),
                        round(float(ligne['price'])*(float(ligne['profit'])
                                                     / 100), 2)))

    max_profit, max_invest, selection = portfolio_analysis(ele, 500)
    print(f"Pour un investissement de {max_invest},"
          f" profit de {round(max_profit,2)} "
          f"avec la selection {selection}")
    print("--- %s secondes ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
