proceeds = int(input('Enter your proceeds: '))
economic_costs = int(input('Enter economic costs: '))

while True:
    economic_profit = proceeds - economic_costs
    if economic_profit > 0:
        print('You have a positive balance')
        if True:
            return_on_revenue = economic_profit / proceeds
            print(return_on_revenue)
            amount = int(input('Enter the number of workers: '))
            balance_of_worker = economic_profit / amount
            print(f'One person of worker have {balance_of_worker} money')
        break
    else:
        print('You have negative balance')
        break
