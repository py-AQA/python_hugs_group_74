import time
from math import sqrt, pi

from selenium import webdriver
from selenium.webdriver.common.by import By

from util import chrome_options


# == Пример композиции ==
class Engine:  # Двигатель
    def start(self):  # Запустить двигатель
        print("Двигатель запущен")

    def stop(self):  # Остановить двигатель
        print("Двигатель остановлен")


class Wheels:  # Колеса
    def turn(self, direction):  # Повернуть колеса
        print(f"Колеса: {direction}")


class Car:  # Машина
    def __init__(self):
        self.engine = Engine()  # Композиция
        self.wheels = Wheels()  # Композиция

    def start(self):  # Начать движение
        print("Начать движение")
        self.engine.start()  # Делегирование
        self.wheels.turn("крутятся вперед")  # Делегирование

    def stop(self):
        print("Остановиться")
        self.wheels.turn("стоят")  # Делегирование
        self.engine.stop()  # Делегирование


def test_car():
    my_car = Car()
    my_car.start()
    my_car.stop()


# == Пример с геометрическими фигурами ==
# Базовый класс
class Shape:  # Абстрактный класс "Фигура"
    # Определяем свойства в базовом классе
    # Чтобы затем воспользоваться наследованием и полиморфизмом
    @property
    def area(self):  # Абстрактный метод "площадь фигуры"
        raise NotImplementedError()  # Фигура абстрактная и вызывать метод "площадь" для неё нельзя

    @property
    def perimeter(self):  # Абстрактный метод "периметр фигуры"
        raise NotImplementedError()  # Фигура абстрактная и вызывать метод "периметр" для неё нельзя


# == Создаём для примера кучу геометрических фигур ==

class Circle(Shape):  # Класс "Круг"
    def __init__(self, radius):  # Конструктор класса
        # Один параметр - радиус круга
        self.__radius = radius  # Запоминаем радиус круга в приватном поле

    @property  # Мы в любой момент можем получить значение радиуса круга
    def radius(self):
        return self.__radius

    @radius.setter  # Можем изменить радиус круга
    def radius(self, radius):
        assert isinstance(radius, int) or isinstance(radius, float), "Радиус должен быть числом"
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        print(f"Радиус круга изменён на {radius}")
        self.__radius = radius

    @property  # Вычисляемое свойство
    def area(self):  # Переопределение метода
        return pi * (self.__radius ** 2)

    @property
    def perimeter(self):  # Переопределение метода
        return 2 * pi * self.__radius  # Длина окружности

    def __str__(self):  # Как показывать при печати
        return f"Круг с радиусом {self.__radius}"


class Rectangle(Shape):  # Класс "Прямоугольник"
    def __init__(self, width, height):  # Конструктор класса
        assert width > 0, "Ширина должна быть положительной"
        assert height > 0, "Высота должна быть положительной"
        self.width = width  # Ширина прямоугольника
        self.height = height  # Высота прямоугольника

    @property
    def area(self):  # Переопределение метода
        return self.width * self.height

    @property
    def perimeter(self):  # Переопределение метода
        return 2 * (self.width + self.height)

    def __str__(self):  # Как показывать при печати
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"


# Класс для представления треугольника
class Triangle(Shape):
    def __init__(self, a, b, c):  # Конструктор класса
        assert a >= 0, "Сторона a должна быть неотрицательной"
        assert b >= 0, "Сторона b должна быть неотрицательной"
        assert c >= 0, "Сторона c должна быть неотрицательной"
        self.a = a  # Стороны так и останутся публичными полями
        self.b = b
        self.c = c

    @property
    def area(self):  # Переопределение метода
        # Считаем площадь треугольника по формуле Герона
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @property
    def perimeter(self):  # Переопределение метода
        return self.a + self.b + self.c

    def __str__(self):  # Как показывать при печати
        return f"Треугольник со сторонами {self.a}, {self.b} и {self.c}"


def test_shapes():
    # Создание объекта класса "Круг"
    circle = Circle(5)
    assert str(circle) == "Круг с радиусом 5"
    assert abs(circle.area - 78.53) < 0.01
    assert abs(circle.perimeter - 31.42) < 0.01
    # circle.radius += 2
    # circle.setRedius(circle.radius() + 2)
    # circle.radius = -2 # Приведёт к ошибке
    # Создание объекта класса "Прямоугольник"
    rectangle = Rectangle(4, 6)
    assert str(rectangle) == "Прямоугольник с шириной 4 и высотой 6"
    assert rectangle.area == 24
    assert abs(rectangle.perimeter - 20) < 0.01
    # Создание объекта класса "Треугольник"
    triangle = Triangle(4, 5, 3)
    assert triangle.area == 6.0
    assert triangle.perimeter == 12
    assert str(triangle) == "Треугольник со сторонами 4, 5 и 3"
    # Отображаем все свойства
    print(f"Площадь круга: {circle.area}")
    print(f"Периметр круга: {circle.perimeter}")
    print(f"Площадь прямоугольника: {rectangle.area}")
    print(f"Периметр прямоугольника: {rectangle.perimeter}")
    print(f"Площадь треугольника: {triangle.area}")
    print(f"Периметр треугольника: {triangle.perimeter}")
    # Полиморфизм на свойствах
    shapes = [circle, rectangle, triangle]  # Массив фигур
    for shape in shapes:  # Пробегаем по массиву фигур
        print(f"{shape} Площадь {shape.area} Периметр {shape.perimeter}")


# === Пример простого контейнера ===
# Практического смысла в нём нет, так как он
# менее функциональный чем встроенный контейнер список
class Bag:  # Контейнер "Сумка
    def __init__(self):  # Конструктор
        self.items = []  # Изначально сумка пустая

    def add(self, item):  # Добавить элемент в сумку
        self.items.append(item)

    def remove(self, item):  # Удалить элемент из сумки
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError(f"{item} не найден в сумке")

    def __str__(self):  # Вывести что есть в сумке
        return ", ".join(self.items)

    def is_empty(self):
        return self.items == []


def test_bag():
    my_bag = Bag()
    assert my_bag.is_empty(), "Сумка должна быть пустой"
    my_bag.add("яблоко")
    assert not my_bag.is_empty(), "Сумка должна содержать яблоко"
    assert str(my_bag) == "яблоко"
    my_bag.add("банан")
    assert str(my_bag) == "яблоко, банан"
    my_bag.remove("яблоко")
    assert str(my_bag) == "банан"
    my_bag.remove("банан")
    assert str(my_bag) == ""


# Примеры перегрузки операторов:
# Перегрузка арифметических операций
class Vector:  # Вектор в двумерном пространстве
    def __init__(self, x, y):  # Конструктор
        self.x = x  # Координата x
        self.y = y  # Координата y

    def __add__(self, other):  # Сложение векторов
        assert isinstance(other, Vector)
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # Вычитание векторов
        assert isinstance(other, Vector)
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):  # Увеличить вектор в scale раз
        assert isinstance(scale, float) or isinstance(scale, int)
        return Vector(self.x * scale, self.y * scale)

    def __truediv__(self, scale):  # Уменьшить вектор в scale раз
        assert isinstance(scale, float) or isinstance(scale, int)
        return Vector(self.x / scale, self.y / scale)

    def len(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    # Можем ещё ввести операцию сравнения если придумаем к ней смысл
    def __lt__(self, other):
        assert isinstance(other, Vector)
        return self.len() < other.len()

    def __le__(self, other):
        assert isinstance(other, Vector)
        return self.len() <= other.len()

    def __gt__(self, other):  # Операция больше
        assert isinstance(other, Vector)
        return self.len() > other.len()

    def __ge__(self, other):  # Операция больше или равно
        assert isinstance(other, Vector)
        return self.len() >= other.len()

    def __str__(self):
        return f"({self.x}, {self.y})"


def test_vector():
    v1 = Vector(2, 3)
    v2 = Vector(1, 1)
    assert str(v1 + v2) == "(3, 4)"
    assert str(v1 - v2) == "(1, 2)"
    assert str(v1 * 2) == "(4, 6)", str(v1 * 2)
    assert str(v1 / 2.0) == "(1.0, 1.5)"


# == Книга - пример операции равенства ==
class Book:
    def __init__(self, name: str, author: str):
        assert isinstance(name, str)
        assert isinstance(author, str)
        self.name = name  # Название книги
        self.author = author  # Автор книги

    # Перегрузка ==
    # Сравнить две книги на равенство
    def __eq__(self, other):
        return self.name == other.name and self.author == other.author

    def __str__(self):
        return f"{self.author} {self.name}"


def test_book():
    book1 = Book("1984", "George Orwell")
    book2 = Book("1984", "George Orwell")
    assert book1 == book2, f"{str(book1)} != {str(book2)}"
    book3 = Book("Война и мир", "Лев Толстой")
    assert book1 != book3


# Перегрузка [] (операторы индексирования)
class CustomList:
    def __init__(self):
        self.data = {}

    def __getitem__(self, index):
        return self.data.get(index, f"Нет элемента с индексом {index}")

    def __setitem__(self, index, value):
        self.data[index] = value


def test_custom_list():
    my_list = CustomList()
    my_list[5] = "Пять"
    assert my_list[5] == "Пять"
    assert my_list[2] == "Нет элемента с индексом 2"


# Представим, что у нас есть страница авторизации.
# Эта страница содержит поля для ввода имени пользователя и пароля,
# а также кнопку входа в систему.
class LoginPage:
    def __init__(self, driver):
        self.driver = driver  # Сохраняем драйвер для дальнейшего использования
        # Открываем сразу нужную страницу входа
        driver.get("https://www.saucedemo.com/")
        self.username_input = (By.XPATH, '//input[@data-test="username"]')
        self.password_input = (By.XPATH, '//input[@data-test="password"]')
        self.login_button = (By.XPATH, '//input[@data-test="login-button"]')

    def open(self):  # Второй вариант
        # Открываем нужную страницу
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str):  # Ввести имя пользователя
        assert isinstance(username, str)
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password: str):  # Ввести пароль
        assert isinstance(password, str)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):  # Войти в систему
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):  # Действие целиком - вход в систему
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


def test_login():
    # Инициализация драйвера Selenium для Chrome
    driver = webdriver.Chrome(options=chrome_options())
    # Создание объекта Page Object
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    # Проверка, что авторизация прошла успешно
    time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    driver.quit()
