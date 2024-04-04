import pytest

from main import BooksCollector


class TestBooksCollector:

            # Проверка 1.0
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        assert collector.get_book_genre('Точка обмана') == ''
            # Проверка 1.1
    def test_add_new_book_negative(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        assert len(collector.get_books_genre()) == 1

        # Проверка 2.0
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.set_book_genre('Точка обмана', 'Детективы')
        assert collector.get_book_genre('Точка обмана') == 'Детективы'
            # Проверка 2.1
    def test_set_book_genre_negative(self):
        collector = BooksCollector()
        collector.set_book_genre('Запятая обмана', 'Детективы')
        assert collector.get_book_genre('Запятая обмана') == ''

            # Проверка 3.0

            # Проверка 4.0
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.set_book_genre('Точка обмана', "Детективы")
        collector.add_new_book('Цифровая крепость')
        collector.set_book_genre('Цифровая крепость', "Фантастика")
        collector.add_new_book('Ангелы и демоны')
        collector.set_book_genre('Ангелы и демоны', "Детективы")
        assert collector.get_books_with_specific_genre("Детективы") == ['Точка обмана', 'Ангелы и демоны']

            # Проверка 5.0
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.add_new_book('Цифровая крепость')
        collector.set_book_genre('Точка обмана', 'Детективы')
        collector.set_book_genre('Цифровая крепость', 'Фантастика')
        assert collector.get_books_genre() == {'Точка обмана': 'Детективы', 'Цифровая крепость': 'Фантастика'}

            # Проверка 6.0
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.set_book_genre('Точка обмана', 'Детективы')
        collector.add_new_book('Цифровая крепость')
        collector.set_book_genre('Цифровая крепость', 'Фантастика')
        collector.add_new_book('Ангелы и демоны')
        collector.set_book_genre('Ангелы и демоны', 'Комедии')
        assert collector.get_books_for_children() == ['Цифровая крепость', 'Ангелы и демоны']

        # Проверка 7.0
    def test_get_books_for_children_if_genre_not_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Членокио')
        collector.set_book_genre('Членокио', 'Ужасы')
        assert collector.get_books_for_children() == []

            # Проверка 8.0
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.add_book_in_favorites('Точка обмана')
        assert collector.get_list_of_favorites_books() == ['Точка обмана']
        # Я предположила, что ошибка была в том, что я банально () не поставила. Могу ошибаться, но больше я не знаю в чем тут ошибка.
            # Проверка 8.1
    def test_add_book_in_favorites_negative(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Точка обмана')
        assert len(collector.get_list_of_favorites_books()) == 1

            # Проверка 9.0
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.add_book_in_favorites('Точка обмана')
        collector.delete_book_from_favorites('Точка обмана')
        assert collector.get_list_of_favorites_books() == []
            # Проверка 9.1
    def test_delete_book_from_favorites_negative(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Точка обмана')
        assert collector.get_list_of_favorites_books() == []

            # Проверка 10.0
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.add_new_book('Цифровая крепость')
        collector.add_book_in_favorites('Точка обмана')
        collector.add_book_in_favorites('Цифровая крепость')
        assert collector.get_list_of_favorites_books() == ['Точка обмана', 'Цифровая крепость']

            # Проверка 11.0
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.add_new_book('Точка обмана')
        assert len(collector.get_books_genre()) == 1

            # Проверка 12.0


    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Точка обмана', 'Детективы'],
            ['Цифровая крепость', 'Фантастика'],
            ['Ангелы и демоны', 'Комедия']
        ]
    )
    def test_set_book_genre_parametrized(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre
