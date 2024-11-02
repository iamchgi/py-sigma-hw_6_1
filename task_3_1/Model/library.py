# --------------------------- Homework_6.1  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Модуль роботи з класом 'Бібліотека':


Package Version
------- -------
pip 23.2.1

"""
from task_3_1.Model.book import Book


#  клас  'Library' утримує змінну список, з екземплярів класу Книга
class Library:
    def __init__(self) -> None:
        self.catalog = []

    def add(self, book : Book) -> None:
        self.catalog.append(book)

    def adds(self, books : tuple) -> None:
        for book in books:
            self.catalog.append(book)

    def delete(self, book) -> None:
        self.catalog.remove(book)

    def found_by_number(self, number : int) -> Book:
        for book in self.catalog:
            if book.get_number() == number:
                return book

    def found_by_name(self, title : str) -> Book:
        for book in self.catalog:
            if book.get_title() == title:
                return book

    def found_by_genre(self, genre : str) -> 'Library':
        books = Library()
        for book in self.catalog:
            if book.get_genre() == genre:
                books.add(book)
        return books

    def found_by_author_and_year(self, author :str, year : int) -> 'Library':
        books = Library()
        for book in self.catalog:
            if book.get_autor() == author and book.get_year() == year:
                books.add(book)
        return books

    # Друк на консоль переліку книг всієї бібліотеки
    def draw(self) -> None:
        print("---------------------------------------------------------------------------------------------------")
        print(f"  №  Автор                 Назва                   Видавник            Жанр            Рік видання")
        print("---------------------------------------------------------------------------------------------------")
        for item in self.catalog:
            item.draw()
        print("")
