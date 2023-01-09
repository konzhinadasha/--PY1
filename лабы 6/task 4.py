import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename, "r") as f:
        list_ = []
        for index, line in enumerate(f): # получаем значния ячеек из строки
            values = line.strip(new_line).split(delimiter)
            if index == 0:  # значения из первой строки сохраняем как заголовки
                names = values
                continue

            list_.append({})  # добавляем новый словарь в список

            for a, b in enumerate(names):
                # берем последний элемент списка (новый словарь), добавляем в него нужный элемент по ключу
                list_[-1][names[a]] = values[a]

    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

# пустая строка
