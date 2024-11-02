# --------------------------- Homework_6.1  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Модуль роботи з 2d фігурами

Package Version
------- -------
pip 23.2.1
"""

import math


#  Введення значення з плаваючою комою, з попереднім друком запрошення і контролем помилки
def input_float(text) -> float:
    try:
        result = float(input(text))
    except ValueError:
        print("Error, некоректні вхідні дані")
    else:
        return result


# Батьківський клас пласкої 2д фігури де area - площа фігури; name - назва(тип) фігури; p - периметр фігури
class Figure2d:
    def __init__(self, name):
        self.name = name
        self.area = None

    def set_properties(self):
        pass

    def area_draw(self):
        round_area = round(self.area, 2)
        print(f"{self.name}. Площа : {round_area}")

    def area_calculate(self):
        pass


# Клас коло, нащадок пласкої фігури
class Circle(Figure2d):
    def __init__(self, name):
        super().__init__(name)
        self.radius = None
        self.p = None

    def set_radius(self, radius):
        self.radius = radius

    # Введення радіуса трикутника
    def set_properties(self) -> None:
        print("Розрахунок площі кола, за значенням радіуса.")
        self.radius = input_float("Введіть значення радіусу кола ->")

    def area_calculate(self):
        self.area = self.radius ** 2 * math.pi

    def area_draw(self):
        super().area_draw()
        print(f"r = {self.radius}")


# Клас трикутник, нащадок пласкої фігури
class Triangle(Figure2d):
    def __init__(self, name):
        super().__init__(name)
        self.p = None
        self.b = None
        self.a = None
        self.c = None

    def set_side_a(self, a):
        self.a = a

    def set_side_b(self, b):
        self.b = b

    def set_side_c(self, c):
        self.c = c

    #  введення значень трьох сторін трикутника
    def set_properties(self):
        print("Розрахунок площі трикутника, за трьома сторонами.")
        self.set_side_a(input_float("Введіть значення сторони а ->"))
        self.set_side_b(input_float("Введіть значення сторони b ->"))
        self.set_side_c(input_float("Введіть значення сторони c ->"))

    # Підрахунок площі трикутника за трьома сторонами
    def area_calculate(self):
        try:
            self.p = (self.a + self.b + self.c) / 2
            self.area = math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
        except ValueError:
            print("Помилка: неможливо обчислити квадратний корінь з від'ємного числа!")
        except TypeError:
            print("Error, некоректні вхідні дані")

    def area_draw(self):
        super().area_draw()
        print(f"a = {self.a}, b = {self.b}, c = {self.c}")


# Клас паралелограм, нащадок пласкої фігури
class Parallelogram(Figure2d):
    def __init__(self, name):
        super().__init__(name)
        self.angle = None
        self.b = None
        self.a = None

    def set_side_a(self, a):
        self.a = a

    def set_side_b(self, b):
        self.b = b

    def set_angle(self, angle):
        self.angle = angle

    #  введення значень двох сторін і кута між ними
    def set_properties(self):
        print("Розрахунок площі паралелограма, за двома сторонами і кутом між ними.")
        self.set_side_a(input_float("Введіть значення сторони а ->"))
        self.set_side_b(input_float("Введіть значення сторони b ->"))
        self.set_angle(input_float("Введіть значення кута ->"))

    def area_calculate(self):
        try:
            angle_in_radians = math.radians(self.angle)
            self.area = self.a * self.b * math.sin(angle_in_radians)
        except ValueError:
            print("Error, некоректні вхідні дані")
        except TypeError:
            print("Error, некоректні вхідні дані")

    def area_draw(self):
        super().area_draw()
        print(f"a = {self.a}, b = {self.b}, α = {self.angle}")
