from typing import Union
import doctest
import math


class Parallelepiped:
    """
    Документация.

    Класс параллелипипед: для определения свойств одноменного тела.
    Применим, если все внутренние углы прямые.
    """
    def __init__(self, length: Union[int, float] = 0, width: Union[int, float] = 0, height: Union[int, float] = 0):
        """ Инициализация экземпляра класса.

        Примеры:
        >>> parallelepiped_1 = Parallelepiped(10, 10, 3.5)
        >>> parallelepiped_2 = Parallelepiped(15.8, 10.3, 23.5)
        """

        if not isinstance(height, (int, float)):
            raise TypeError('Размер ребра должен быть типа int или float')
        if not isinstance(width, (int, float)):
            raise TypeError('Размер ребра должен быть типа int или float')
        if not isinstance(length, (int, float)):
            raise TypeError('Размер ребра должен быть типа int или float')
        if height < 0 or width < 0 or length < 0:
            raise ValueError('Размер ребра не может быть меньше или равен нулю')

        self.height = height
        self.width = width
        self.length = length
        self._name = None  # этот атрибут protected, потому что определяется программой автоматически и не задается
        # пользователем в явном виде

    @property  # для защищенного атрибута пишем getter. Теперь реализована защита
    def name(self) -> str:
        """ Метод для чтения защищенного атрибута.

        Возвращает его значение.
        """
        return self._name

    @name.setter
    def name(self, value) -> None:
        """ Метод для записи значения защищенного атрибута.

        Принимает переменную от пользователя, но ничего не возвращает.
        В данной программе пользователь не имеет возможности задавать это значение, это заблокировано в явном виде.
        """
        if value is not None:  # защита в явном виде. Нельзя поменять значение
            raise AttributeError('Доступ к редактированию запрещен')

        # назначение значения атрибуту self._name
        if self.height > 0 and self.width > 0 and self.length > 0:
            self._name = 'Параллелипипед'
        elif self.height == 0 and self.width > 0 and self.length > 0:
            self._name = 'Прямоугольник'
        elif self.height == 0 and self.width == 0 and self.length > 0:
            self._name = 'Прямая'

    def __str__(self):
        """ Метод вопспроизведения объекта в виде сроки.

        Чтение предназначено для человека.

        Примеры:
        >>> parallelepiped_1 = Parallelepiped(10, 10, 3.5)
        >>> print(parallelepiped_1)
        """
        return f"Геометрический объект {self.name}. Длина {self.length}, глубина {self.width}, высота {self.height}"

    def __repr__(self):
        """ Метод вопспроизведения объекта в виде валидной сроки.

        Чтение предназначено для интерпретатора. По такой строке можно инициализировать новый экземпляр класса.

        Примеры:
        >>> parallelepiped_1 = Parallelepiped(10, 10, 3.5)
        >>> print(repr(parallelepiped_1))
        """
        return f"{self.__class__.__name__}(length={self.length!r}, width={self.width!r}, height={self.height!r})"

    def volume(self) -> Union[int, float]:
        """ Метод возвращает объем тела.

        Примеры:
        >>> parallelepiped_2 = Parallelepiped(15.8, 10.3, 23.5)
        >>> print(parallelepiped_2.volume())
        """
        return self.height * self.width * self.length

    def perimeter(self) -> Union[int, float]:
        """ Метод возвращает сумму длинн всех ребер тела.

        Примеры:
        >>> parallelepiped_2 = Parallelepiped(15.8, 10.3, 23.5)
        >>> print(parallelepiped_2.perimeter())
        """
        return (self.height + self.width + self.length) * 4

    def cross_section(self) -> Union[int, float]:
        """ Метод определяет поперечное сечение тела.
        Вычисляет площадь этого сечения.

        Примеры:
        >>> parallelepiped_1 = Parallelepiped(10, 10, 3.5)
        >>> parallelepiped_2 = Parallelepiped(15.8, 10.3, 23.5)
        >>> parallelepiped_1.cross_section()
        >>> parallelepiped_2.cross_section()
        """
        if self.width == self.length:
            print("Сечение параллелипипеда/выбранная сторона - квадрат")
        else:
            print("Сечение параллелипипеда/выбранная сторона - прямоугольник")
        return self.length * self.width


class Rectangle(Parallelepiped):
    """
    Документация.

    Класс квадрат: для определения свойств одноменной фигуры.
    Дочерний от класса параллелипипед.
    Применим, если все внутренние углы прямые.
    """
    def __init__(self, length: Union[int, float] = 0, width: Union[int, float] = 0, colour: str = 'белый'):
        """ Инициализация экземпляра класса.

        Примеры:
        >>> rectangle_1 = Rectangle(10, 10)
        >>> rectangle_2 = Rectangle(15.8, 10.3, 'синий')
        """

        super().__init__(length, width)  # наследуем эти атрибуты и их проверки из базового класса
        # и унаследуем атрибут self._name, так как условия присвоения ему значения из родительского класса справедливы

        if not isinstance(colour, str):
            raise TypeError('Цвет фигуры должен быть задан в виде строки')

        self.colour = colour

    # наследуем str метод, для чтения человеком информации достаточно

    def __repr__(self):
        """ Метод вопспроизведения объекта в виде валидной сроки.

        Чтение предназначено для интерпретатора. По такой строке можно инициализировать новый экземпляр класса.

        Примеры:
        >>> rectangle_2 = Rectangle(15.8, 10.3, 'синий')
        >>> print(repr(rectangle_2))
        """
        return f"{self.__class__.__name__}(length={self.length!r}, width={self.width!r}, colour={self.colour!r})"

    # наследуем метод cross_section - он также будет работать, подсчитает площадь прямоугольника
    # метод volume как бы тоже наследуется, но он выдаст нулевое значение - его не используем. Площадь фигуры уже нашли

    def perimeter(self) -> Union[int, float]:  # перегружаем, так как другая формула вычичисления
        """ Метод возвращает сумму длинн всех сторон фигуры.

        Примеры:
        >>> rectangle_2 = Rectangle(15.8, 10.3, 'синий')
        >>> print(rectangle_2.perimeter())
        """
        return (self.width + self.length) * 2

    def diagonal(self) -> Union[int, float]:  # собственный метод дочернего класса
        """ Метод возвращает значение длинны диагонали фигуры.

        Примеры:
        >>> rectangle_2 = Rectangle(15.8, 10.3, 'синий')
        >>> print(rectangle_2.diagonal())
        """
        return math.sqrt(self.length ** 2 + self.width ** 2)


if __name__ == "__main__":
    doctest.testmod()

    # проверка работы базового класса в явном виде
    parallelepiped_one = Parallelepiped(10, 10)
    parallelepiped_two = Parallelepiped(15.8, 10.3, 23.5)
    print(parallelepiped_one, '\n', parallelepiped_two, '\n', repr(parallelepiped_one), '\n', repr(parallelepiped_two))
    print(parallelepiped_one.name, '\n', parallelepiped_two.name)
    print(parallelepiped_two.volume(), '\n', parallelepiped_two.perimeter(), '\n', parallelepiped_two.cross_section())

    # проверка работы дочернего класса в явном виде
    rectangle_one = Rectangle(10, 10)
    rectangle_two = Rectangle(15.8, 10.3, 'синий')
    print(rectangle_one, '\n', rectangle_two, '\n', repr(rectangle_one), '\n', repr(rectangle_two))
    print(rectangle_one.name, '\n', rectangle_two.name)
    print(rectangle_two.diagonal(), '\n', rectangle_two.perimeter(), '\n', rectangle_two.cross_section())

    pass
# пустая строка
