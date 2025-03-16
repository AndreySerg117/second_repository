import uuid


class Book:
    def __init__(self, name: str, book_name: str):
        self.name: str = name
        self.book_name: str = book_name
        self.inn: uuid.UUID = uuid.uuid4()

    def __str__(self):
        return f'<Book {self.book_name} - {self.inn}>'


book = Book('Andjey Sapkowskiy', 'Witcher')
pass


class Library:
    def __init__(self, name: str):
        self.name = name
        self.list_book: list[book] = []

    def add_book(self, book: Book):
        self.list_book.append(book)

    def delete_book(self, book_inn):
        for book in self.list_book:
            if book.inn == book.inn:
                self.list_book.remove(book)
                break

