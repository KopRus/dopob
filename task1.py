BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строку формата, где "название_книги" берется с помощью атрибута name.
        >>> book = Book(id_=1, name='test_name_1', pages=200)
        >>> str(book)
        'Книга "test_name_1"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр.
        >>> book = Book(id_=1, name='test_name_1', pages=200)
        >>> repr(book)
        'Book(id_=1, name='test_name_1', pages=200)'
        """
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'



if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
