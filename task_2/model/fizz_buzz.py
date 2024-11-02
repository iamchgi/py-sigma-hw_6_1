# --------------------------- Homework_6.1  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Модуль роботи з алгоритмом FizzBuzz.

Логіка роботи алгоритму:
На вхід алгоритму подається деяке число n – набране із клавіатури, або задане
множиною. Необхідно сформувати вихідну послідовність, що відповідає властивостям числа n:
якщо число можна поділити на 3 без залишку, замість числа буде виведено Fizz.
якщо число ділиться на 5 без залишку, результат відображатиме Buzz замість числа.
якщо дане число ділиться і на 3, і на 5, замість числа буде надруковано FizzBuzz.
якщо число не можна поділити на 3 або 5, воно буде надруковано в оригіналі.
Приклад:
задано набір чисел:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Ваш код має створити нову колекцію з таким результатом:
["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
"""


class FizzBuzz:
    def __init__(self):
        self.result = None  # результативний набір із заміненими значеннями відповідно до завдання
        self.source = None  # вхідний набір чисел

    def show_source(self):
        print(f"Вхідний набір чисел: \n {self.source}")

    def show_result(self):
        print(f"Результат, вихідний набір:\n {self.result}")

    def set_source(self, param):
        self.source = param

    #    Функція обчислення послідовності по алгоритму FizzBuzz
    def calculate(self):
        result = list()
        for item in self.source:
            div_by_3 = item % 3 == 0
            div_by_5 = item % 5 == 0
            div_by_both = div_by_3 and div_by_5
            if div_by_both:
                result.append("FizzBuzz")
            elif div_by_3:
                result.append("Fizz")
            elif div_by_5:
                result.append("Buzz")
            else:
                result.append(item)
        self.result = tuple(result)
