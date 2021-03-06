import time
import csv


""" Scripte brute de force pour maximiser les profits sur le fichiers
 liste_actions

"""


def binary_code_chart(elements, invest_max):
    """A partir de l'ensemble des actiions disponible, va générer l'ensemble des
    combinaisons possibles et ne conserver que les valides (qui ne dépassent
    pas l'investissement max.)

    Args:
        elements (list): Les actions avec nom, prix et profit
        invest_max (int): Le montant maximum pouvant être investi

    Returns:
        [list]: La liste des combinaisons valides sous forme binaire
    """
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


# une fois que la liste des combinaisons possibles est établie :
# - Calcul du prix de la combinaison
def combination_invest(selection):
    """Calcul le prix de la combinaison qui lui est adressée en cumulant
    chaque prix

    Args:
        selection (list): combinaison d'actions

    Returns:
        [type]: Prix total de la combinaison d'actions
    """
    total_price = 0
    for prices in selection:
        total_price += prices[1]
    return total_price


# - Calcul du profit de la combinaison
def combination_profit(selection):
    """Calcul le profit de la combinaison qui lui est adressée en cumulant
    chaque profit

    Args:
        selection (list): combinaison d'actions

    Returns:
        [type]: Profit total de la combinaison d'actions
    """
    total_profit = 0
    for profits in selection:
        total_profit += profits[2]
    return total_profit


# Optimisation de la selection

def best_combination(combinations):
    """Cherche meilleure solutions en remplaçant le meilleur profit au fur et
    à mesure qu'un meilleur profit est trouvé

    Args:
        combinations (list): ensemble des combinaisons d'acions retenues

    Returns:
        [float, float, list]: le meilleur profit, le total investi, le détail
                                de la combinaison
    """
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
    """Lance l'analyse du portefeuille en appelalnt la fonction qui va générer
    les combinaisons sous forme binaire, puis en recréant les combinisons sous
    forme de listes détaillées, puis les adresses à best_cobination pour déterminer
    la meilleure de toutes

    Args:
        elements (list): ensemble des actions
        invest_max (int): montant maximum pouvant être investi

    Returns:
        [tuple]: le meilleur profit, le total investi, le détail de la combinaison
    """
    options = []
    chart = binary_code_chart(elements, invest_max)
    # Traduction des combinaisons possibles binaires en éléments
    for code in chart:
        option = []
        for index, value in enumerate(code):
            if value == str(1):
                option.append(elements[index])
        options.append(option)

    solution = best_combination(options)
    print(type(solution), solution)

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
