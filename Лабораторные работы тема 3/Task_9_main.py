salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(months):  # цикл по количеству месяцев
    money_capital += (spend - salary)  # прибовляем к количеству денег читсые расходы за текущий месяц
    spend *= (1 + increase)  # увеличиваем траты

print(round(money_capital))
