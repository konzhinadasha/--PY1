from typing import Union
import doctest


class Parallelepiped:
    """
    Документация.
    Класс параллелипипед: для определения свойств одноменного тела.
    Применим, если все внутренние углы прямые.
    """
    def __init__(self, height: Union[int, float], width: Union[int, float], length: Union[int, float]):
        """ Инициализация экземпляра класса.

        Примеры:
        >>> parallelepiped_1 = Parallelepiped(5, 10, 3.5)
        >>> parallelepiped_2 = Parallelepiped(5, 10, 10)
        """
        if not isinstance(height, (int, float)):
            raise TypeError('Размер ребра должен быть типа int или float')
        if not isinstance(width, (int, float)):
            raise TypeError('Размер ребра должен быть типа int или float')
        if not isinstance(length, (int, float)):
            raise TypeError('Размер ребра должен быть типа int или float')
        if height <= 0 or width <= 0 or length <= 0:
            raise ValueError('Размер ребра не может быть меньше или равен нулю')

        self.height = height
        self.width = width
        self.length = length

    def volume(self) -> Union[int, float]:
        """ Метод возвращает объем тела.

        Примеры:
        >>> parallelepiped_1 = Parallelepiped(5, 10, 3.5)
        >>> print(parallelepiped_1.volume())
        """
        return self.height * self.width * self.length

    def perimeter(self) -> Union[int, float]:
        """ Метод возвращает сумму длинн всех ребер тела.

        Примеры:
        >>> parallelepiped_1 = Parallelepiped(5, 10, 3.5)
        >>> print(parallelepiped_1.perimeter())
        """
        return (self.height + self.width + self.length) * 4

    def cross_section(self) -> None:
        """ Метод определяет поперечное сечение тела.

        Примеры:
        >>> parallelepiped_1 = Parallelepiped(5, 10, 3.5)
        >>> parallelepiped_2 = Parallelepiped(5, 10, 10)
        >>> parallelepiped_1.cross_section()
        >>> parallelepiped_2.cross_section()
        """
        if self.width == self.length:
            print("Сечение параллелипипеда - квадрат")
        else:
            print("Сечение параллелипипеда - прямоугольник")


class Stars:
    """
    Документация.
    Класс звезды: различными способами печатает вводимые символы в вводимом количестве.
    Применим для любых символов, записанных в виде строки.
    """
    def __init__(self, amount: int, pictogram: str):
        """ Инициализация экземпляра класса.

        Примеры:
        >>> star_1 = Stars(10, '@')
        """
        if not isinstance(amount, int):
            raise TypeError('Количество символов должено быть типа int, то есть целым')
        if not isinstance(pictogram, str):
            raise TypeError('Символ должен быть задан в виде строки')
        if amount <= 0:
            raise ValueError('Количество символов не может быть не положительным')
        if len(pictogram) > 1:
            raise ValueError('Строка должна содержать всего 1 символ')

        self.amount = amount
        self.pictogram = pictogram

    def column(self) -> None:
        """ Метод печатает заданное количество строк с одним символом.

        Примеры:
        >>> star_1 = Stars(10, '@')
        >>> star_1.column()
        """
        for _ in range(self.amount):
            print(self.pictogram)

    def srting(self) -> None:
        """ Метод печатает заданное количество символов в одну строку.

        Примеры:
        >>> star_1 = Stars(10, '@')
        >>> star_1.srting()
        """
        print(self.pictogram * self.amount)

    def stair(self) -> None:
        """ Метод печатает лесенку. Количество элементов в строке увеличивается по мере увеличения номера строки.

        Примеры:
        >>> star_1 = Stars(10, '@')
        >>> star_1.stair()
        """
        for i in range(1, self.amount):
            print(self.pictogram * i)


class Marks:
    """
    Документация.
    Класс оценки: для работы со списком строк-значений оценок.
    Применим для неотрицательных оценок по любой шкале.
    """
    def __init__(self, list_: list):
        """ Инициализация экземпляра класса.

        Примеры:
        >>> list_of_marks_1 = Marks(['5', '4', '4', '3', '2', '5', '4', '4', '3', '2', '4', '2', '3', '4', '2', '3', '5', '4', '5',
                         '3', '5', '4', '5', '4', '4', '5', '3'])
        """
        if not isinstance(list_, list):
            raise TypeError('Список оценок должен быть представлен типом list')
        for mark in range(len(list_)):
            if not isinstance(list_[mark], str):
                raise TypeError('Оценки должены быть представлены типом str')
        for mark in range(len(list_)):
            if len(list_[mark]) > 1:
                raise ValueError('Строка должна содержать всего 1 символ')

        list_1 = [int(mark) for mark in list_]
        for mark in range(len(list_)):
            if list_1[mark] < 0:
                raise ValueError('Значение оценки не может быть не положительным')

        self.list_ = list_

    def amount(self) -> dict:
        """ Метод подсчитывает количество одинаковых оценок в списке.
        Возвращает словарь кортежей с парами оценка-количество.

        Примеры:
        >>> list_of_marks_1 = Marks(['5', '4', '4', '3', '2', '5', '4', '4', '3', '2', '4', '2', '3', '4', '2', '3', '5', '4', '5',
                         '3', '5', '4', '5', '4', '4', '5', '3'])
        >>> print(list_of_marks_1.amount())
        """
        dict_of_marks = {}
        for mark in range(len(self.list_)):
            if dict_of_marks.get(self.list_[mark]) is None:
                dict_of_marks[self.list_[mark]] = 1
            else:
                dict_of_marks[self.list_[mark]] += 1
        return dict_of_marks

    def arithmetic(self) -> float:
        """ Метод вычисляет среднее арифметическое значение оценок в списке.
        Возвращает число с плавающей запятой.

        Примеры:
        >>> list_of_marks_1 = Marks(['5', '4', '4', '3', '2', '5', '4', '4', '3', '2', '4', '2', '3', '4', '2', '3', '5', '4', '5',
                         '3', '5', '4', '5', '4', '4', '5', '3'])
        >>> print(list_of_marks_1.arithmetic())
        """
        counter = 0
        list_ = [int(mark) for mark in self.list_]
        for mark in range(len(list_)):
            counter += list_[mark]
        return counter / len(list_)

    def append(self, new_mark: str) -> list:
        """ Метод добавляет новую оценку в конец списка.
        Возвращает дополненный список.

        Примеры:
        >>> list_of_marks_1 = Marks(['5', '4', '4', '3', '2', '5', '4', '4', '3', '2', '4', '2', '3', '4', '2', '3', '5', '4', '5',
                         '3', '5', '4', '5', '4', '4', '5', '3'])
        >>> print(list_of_marks_1.append('5'))
        """
        if not isinstance(new_mark, str):
            raise TypeError('Оценки должены быть представлены типом str')
        if len(new_mark) > 1:
            raise ValueError('Строка должна содержать всего 1 символ')
        new_mark_int = int(new_mark)
        if new_mark_int < 0:
            raise ValueError('Значение оценки не может быть не положительным')

        return self.list_ + list(new_mark)


if __name__ == "__main__":
    doctest.testmod()
    pass
# пустая строка
