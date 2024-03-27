from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    #def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
     #   collector = BooksCollector()

        # добавляем две книги
      #  collector.add_new_book('Гордость и предубеждение и зомби')
      #  collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
       # assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

            # Проверка 1.0
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        assert collector.books_genre.get('Точка обмана') == ''
            # Проверка 1.1
        collector.add_new_book('Точка обмана')
        assert len(collector.books_genre) == 1

            # Проверка 2.0
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.set_book_genre('Точка обмана', 'Детективы')
        assert collector.books_genre.get('Точка обмана') == 'Детективы'
            # Проверка 2.1
        collector.set_book_genre('Запятая обмана', 'Детективы')
        assert collector.books_genre.get('Запятая обмана') == ''

            # Проверка 3.0
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.set_book_genre('Точка обмана', 'Детективы')
        assert collector.get_book_genre('Точка обмана') == 'Детективы'


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
        assert collector.get_book_genre == {'Точка обмана': 'Детективы', 'Цифровая крепость': 'Фантастика'}

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
        books = collector.get_books_for_children()
        assert books == []

            # Проверка 8.0
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.add_book_in_favorites('Точка обмана')
        assert collector.favorites == ['Точка обмана']
            # Проверка 8.1
        collector.add_book_in_favorites('Точка обмана')
        assert len(collector.favorites) == 1

            # Проверка 9.0
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.add_book_in_favorites('Точка обмана')
        collector.delete_book_from_favorites('Точка обмана')
        assert collector.favorites == []
            # Проверка 9.1
        collector.delete_book_from_favorites('Точка обмана')
        assert collector.favorites == []

            # Проверка 10.0
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.add_new_book('Цифровая крепость')
        collector.add_book_in_favorites('Точка обмана')
        collector.add_book_in_favorites('Цифровая крепость')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Точка обмана', 'Цифровая крепость']

            # Проверка 11.0
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Точка обмана')
        collector.add_new_book('Точка обмана')
        assert len(collector.get_books_genre()) == 1

            # Проверка 12.0
    import pytest

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
        assert collector.get_book_genre(name)
