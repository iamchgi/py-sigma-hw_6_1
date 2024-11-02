# --------------------------- Homework_6.1  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Модуль роботи з класом 'Orders':


Package Version
------- -------
pip 23.2.1

"""


# Усі пошукові методи повертають об'єкт класу "Orders"

#  клас  'Orders' утримує змінну словник, з індексів і словарів, що містять замовлення
class Orders:
    def __init__(self):
        self.catalog = {}

    def add(self, number, order):
        self.catalog.update({number: order})

    def adds(self, orders):
        for order in orders:
            self.catalog.update({order})

    def delete(self, number):
        del self.catalog[number]

    def found_by_number(self, number):
        orders = Orders()
        for key, value in self.catalog.items():
            if key == number:
                orders.add(key, value)
                return orders

    def found_by_customer(self, customer):
        orders = Orders()
        for key, value in self.catalog.items():
            if value['customer'] == customer:
                orders.add(key, value)
        return orders

    def found_by_cost(self, cost):
        orders = Orders()
        for key, value in self.catalog.items():
            if value['price'] * value['count'] >= cost:
                orders.add(key, value)
        return orders

    def found_by_title_and_date(self, title, date):
        orders = Orders()
        for key, value in self.catalog.items():
            if value['title'] == title and value['date'] == date:
                orders.add(key, value)
        return orders

    # Друк на консоль переліку замовлення що містяться у словарі
    def draw(self):
        for key, value in self.catalog.items():
            print(f"Замовлення №{key} : Замовник:\"{value['customer']}\" Товар:\"{value['title']}\" "
                  f"Кількість:\"{value['count']}\" Ціна:\"{value['price']}\" Дата:\"{value['date']}\"")
        print("")
