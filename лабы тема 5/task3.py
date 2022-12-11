from random import randint  # импортируем метод генерации рандомных чисел в виде списка из модуля рандом


def get_unique_list_numbers() -> list[int]:
    positive = 10  # верхняя граница диапазона
    negative = -10  # нжняя граница диапазона
    count = 15  # требуемое количество чисел в списке
    set_ = {}
    while True:
        set_ = {randint(negative, positive) for _ in range(count)}
        if len(set_) >= count:
            break
    list_ = [i for i in set_]
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
