money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while True:
    delta = spend - salary  # чистые расходы за месяц
    if delta > money_capital:  # выход из цикла если деньги кончились
        break

    month += 1  # увеличивываем количество прожитых месяцев
    money_capital -= delta  # вычитыаем из подушки чистые расходы за месяц
    spend *= 1 + increase  # учитываем инфлиацию

print(month)  # 8
