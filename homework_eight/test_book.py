class TestBook:
    def test_name(self, book):
        assert book.name == 'Andjey Sapkowskiy'
        assert book.book_name == 'Witcher'


class TestLibrary:
    def test_book_in_library(self, book, library):
        library.add_book(book)
        assert book in library.list_book

    def test_delete_book(self, book, library):
        library.delete_book(book.inn)

    def test_library(self, book):
        assert book.book_name == 'Witcher'
