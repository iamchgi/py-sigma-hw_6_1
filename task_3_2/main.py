# --------------------------- Homework_6.1  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Homework_6.1
Розробити клас «інтернет-замовлення». Передбачити обробник
(конструктор), який приймає ціле число – порядковий номер замовлення та словник, що
містить інформацію про замовлення наступному форматі:
1) прізвище клієнта;
2) назва товару;
3) кількість;
4) вартість;
5) дата замовлення.
Реалізувати можливість роботи із замовленнями: пошук за декількома параметрами
(за прізвищем замовника, за датою замовлення, за товаром тощо), додавання нових
замовлень, видалення інформації про замовлення, доступу до інформації про замовлення за
номером
Передбачити демонстрацію (вивід до консолі) всіх сформованих елементів класу

Package Version
------- -------
pip 23.2.1

"""
from task_3_2.Model.orders import Orders


# --------------------------------- main module ----------------------------------------------
if __name__ == '__main__':
    print(" Робота з класом Orders ")
    orders = Orders()
    orders.add(1,{"customer" : "Mark Twain", "title":"The Adventures to Egypt", "count":1, "price":1000, "date":"1876.10.01"})
    orders.add(2,{"customer":"Mark Twain", "title":"Banana","count":1, "price":500, "date":"1876.10.02"})
    orders.add(3,{"customer": "Arthur Conan Doyle", "title": "Banana", "count": 5, "price": 10, "date": "1876.10.02"})
    orders.add(4,{"customer": "Arthur Conan Doyle", "title": "Banana", "count": 1, "price": 15, "date": "1876.10.03"})
    orders.add(5,{"customer": "Шерлок Холмс", "title": "Banana", "count": 2, "price": 80, "date": "1876.10.04"})
    orders.add(6,{"customer": "Tom Sawyer", "title": "Banana", "count": 4, "price": 30, "date": "1876.10.04"})
    orders.add(7,{"customer": "Tom Sawyer", "title": "Banana", "count": 10, "price": 1, "date": "1876.10.07"})
    orders.add(8,{"customer": "Шерлок Холмс", "title": "Banana", "count": 11, "price": 0.5, "date": "1876.10.07"})
    orders.add(9,{"customer": "Tom Sawyer", "title": "Banana", "count": 100, "price": 110, "date": "1876.10.14"})
    orders.add(10,{"customer": "Tom Sawyer", "title": "Banana", "count": 9, "price": 12, "date": "1876.10.22"})
    orders.draw()
    print("Видаляємо заказ №5")
    orders.delete(5)
    orders.draw()
    print("Знайти за номером: \"2\"")
    orders.found_by_number(2).draw()
    print("Знайти за покупцем: \"Tom Sawyer\"")
    orders.found_by_customer('Tom Sawyer').draw()
    print("Знайти за товаром \"Banana\" і датою продажу \"1876.10.04\"")
    orders.found_by_title_and_date('Banana', "1876.10.04").draw()
    print("Знайдемо всі продажі більше 50$")
    orders.found_by_cost(50).draw()

''' 
РЕЗУЛЬТАТ

 Робота з класом Orders 
Замовлення №1 : Замовник:"Mark Twain" Товар:"The Adventures to Egypt" Кількість:"1" Ціна:"1000" Дата:"1876.10.01"
Замовлення №2 : Замовник:"Mark Twain" Товар:"Banana" Кількість:"1" Ціна:"500" Дата:"1876.10.02"
Замовлення №3 : Замовник:"Arthur Conan Doyle" Товар:"Banana" Кількість:"5" Ціна:"10" Дата:"1876.10.02"
Замовлення №4 : Замовник:"Arthur Conan Doyle" Товар:"Banana" Кількість:"1" Ціна:"15" Дата:"1876.10.03"
Замовлення №5 : Замовник:"Шерлок Холмс" Товар:"Banana" Кількість:"2" Ціна:"80" Дата:"1876.10.04"
Замовлення №6 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"4" Ціна:"30" Дата:"1876.10.04"
Замовлення №7 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"10" Ціна:"1" Дата:"1876.10.07"
Замовлення №8 : Замовник:"Шерлок Холмс" Товар:"Banana" Кількість:"11" Ціна:"0.5" Дата:"1876.10.07"
Замовлення №9 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"100" Ціна:"110" Дата:"1876.10.14"
Замовлення №10 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"9" Ціна:"12" Дата:"1876.10.22"

Видаляємо заказ №5
Замовлення №1 : Замовник:"Mark Twain" Товар:"The Adventures to Egypt" Кількість:"1" Ціна:"1000" Дата:"1876.10.01"
Замовлення №2 : Замовник:"Mark Twain" Товар:"Banana" Кількість:"1" Ціна:"500" Дата:"1876.10.02"
Замовлення №3 : Замовник:"Arthur Conan Doyle" Товар:"Banana" Кількість:"5" Ціна:"10" Дата:"1876.10.02"
Замовлення №4 : Замовник:"Arthur Conan Doyle" Товар:"Banana" Кількість:"1" Ціна:"15" Дата:"1876.10.03"
Замовлення №6 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"4" Ціна:"30" Дата:"1876.10.04"
Замовлення №7 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"10" Ціна:"1" Дата:"1876.10.07"
Замовлення №8 : Замовник:"Шерлок Холмс" Товар:"Banana" Кількість:"11" Ціна:"0.5" Дата:"1876.10.07"
Замовлення №9 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"100" Ціна:"110" Дата:"1876.10.14"
Замовлення №10 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"9" Ціна:"12" Дата:"1876.10.22"

Знайти за номером: "2"
Замовлення №2 : Замовник:"Mark Twain" Товар:"Banana" Кількість:"1" Ціна:"500" Дата:"1876.10.02"

Знайти за покупцем: "Tom Sawyer"
Замовлення №6 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"4" Ціна:"30" Дата:"1876.10.04"
Замовлення №7 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"10" Ціна:"1" Дата:"1876.10.07"
Замовлення №9 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"100" Ціна:"110" Дата:"1876.10.14"
Замовлення №10 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"9" Ціна:"12" Дата:"1876.10.22"

Знайти за товаром "Banana" і датою продажу "1876.10.04"
Замовлення №6 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"4" Ціна:"30" Дата:"1876.10.04"

Знайдемо всі продажі більше 50$
Замовлення №1 : Замовник:"Mark Twain" Товар:"The Adventures to Egypt" Кількість:"1" Ціна:"1000" Дата:"1876.10.01"
Замовлення №2 : Замовник:"Mark Twain" Товар:"Banana" Кількість:"1" Ціна:"500" Дата:"1876.10.02"
Замовлення №3 : Замовник:"Arthur Conan Doyle" Товар:"Banana" Кількість:"5" Ціна:"10" Дата:"1876.10.02"
Замовлення №6 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"4" Ціна:"30" Дата:"1876.10.04"
Замовлення №9 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"100" Ціна:"110" Дата:"1876.10.14"
Замовлення №10 : Замовник:"Tom Sawyer" Товар:"Banana" Кількість:"9" Ціна:"12" Дата:"1876.10.22"

'''
