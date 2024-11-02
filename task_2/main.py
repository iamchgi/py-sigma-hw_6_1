# --------------------------- Homework_6.1  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Homework_6.1
Група вимог 1.
З використанням механізмів модульного, функціонального та ООП програмування
реалізувати програмну архітектуру проекту python у відповідно до структурної схеми:
Група вимог 2.
В блоках: CV, 2D площі, FizzBuzz – послідовність обчислювальних операцій подати
(«огорнути») класом / класами.
Для групи вимог 1 з використанням механізмів наслідування / інкапсуляції /
поліморфізму передбачити можливості:
формування резюме для будь-якої персони;
розрахунок площі декількох фігур.

Package Version
------- -------
pip 23.2.1

"""

import task_2.model.figures_2d as fg2d
from task_2.model import curriculum_vitae as cv
from task_2.model.fizz_buzz import FizzBuzz

# --------------------------------- main module ----------------------------------------------
if __name__ == '__main__':
    # ------------------------  CV ----------------------------
    software_developer = cv.SoftwareDeveloper('Hryhorii Chernolutskyi', '1976', '48')
    software_developer.set_language(("Python", "Pascal", "Java", "VB", "PHP"))

    professor = cv.Profffesssor('Василь Пупкін', '2000', '24')
    professor.set_teaching('10')
    professor.set_subjects(("history", "psychology", "microbiology", "genetics", "philosophy"))

    locksmith = cv.Locksmith('Дід Панас', '1917', '107')
    locksmith.set_tools(('hammer', 'knife', 'screwdriver', 'pliers'))

    for vocation in (software_developer, professor, locksmith):
        vocation.draw()
    # ------------------------ Розрахунок площі пласких фігур ----------------------------
    triangle = fg2d.Triangle("Трикутник")
    parallelogram = fg2d.Parallelogram("Паралелограм")
    circle = fg2d.Circle("Коло")
    for figure in (triangle, parallelogram, circle):
        figure.set_properties()
        figure.area_calculate()
        figure.area_draw()
    # ------------------------ Демонстрація роботи алгоритму FizzBuzz ----------------------------
    print("Демонстрація роботи алгоритму FizBuzz.")
    fb = FizzBuzz()
    fb.set_source(tuple(range(1, 16)))
    fb.calculate()
    fb.show_source()
    fb.show_result()

''' 
РЕЗУЛЬТАТ

Software developer
 Ім'я, прізвище: Hryhorii Chernolutskyi
 Дата народження: 1976
 Вік: 48
 Мови програмування:
Python Pascal Java VB PHP  
Профффесссор
 Ім'я, прізвище: Василь Пупкін
 Дата народження: 2000
 Вік: 24
 Викладацький стаж: 10
 Викладає таке от:
history psychology microbiology genetics philosophy  
locksmith
 Ім'я, прізвище: Дід Панас
 Дата народження: 1917
 Вік: 107
 Має інструменти:
hammer knife screwdriver pliers  
Розрахунок площі трикутника, за трьома сторонами.
Введіть значення сторони а ->10
Введіть значення сторони b ->5
Введіть значення сторони c ->6
Трикутник. Площа : 11.4
a = 10.0, b = 5.0, c = 6.0
Розрахунок площі паралелограма, за двома сторонами і кутом між ними.
Введіть значення сторони а ->10
Введіть значення сторони b ->10
Введіть значення кута ->89.9
Паралелограм. Площа : 100.0
a = 10.0, b = 10.0, α = 89.9
Розрахунок площі кола, за значенням радіуса.
Введіть значення радіусу кола ->1
Коло. Площа : 3.14
r = 1.0
Демонстрація роботи алгоритму FizBuzz.
Вхідний набір чисел: 
 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
Результат, вихідний набір:
 (1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz')

'''
