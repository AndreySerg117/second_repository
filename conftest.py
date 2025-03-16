import pytest

from homework_eight.homework_eight import Book, Library


@pytest.fixture()
def book() -> Book:
    witcher = Book('Andjey Sapkowskiy', 'Witcher')
    return witcher


@pytest.fixture()
def library() -> Library:
    books = Library(name='KSD')
    return books
