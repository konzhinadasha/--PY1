# написать то что переводит число из десятияной в остальные
# написать список в который включен цикл прогона от 0 до 15

from pprint import pprint

list_ =[]
for input_ in range (0, 16):
    dictionary = {}
    dictionary['bin'] = bin(input_)
    dictionary['dec'] = input_
    dictionary['hex'] = hex(input_)
    dictionary['oct'] = oct(input_)
    list_.append(dictionary)


pprint(list_)