def delete(list_, index=None):
    if index is None:
        del list_[-1]  # если индекс не задан удаляем последний элемент
    else:
        del list_[index]  # если задан - по заданному
    return list_


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
# пустая строка
