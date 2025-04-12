class Book:
    # This classes name is self-explanitory
    def _init_(self, title: str, author: str,
               genre: str, publish_year: int,
               publisher: str, type: str, price: int,
               stock: int, ISBN: str, edition: str,
               age_rating: int, discount: str):

        self._title = title
        self._author = author
        self._genre = genre
        self._publish_year = publish_year
        self._publisher = publisher
        self._type = type
        self._price = price
        self._stock = stock
        self._ISBN = ISBN
        self._edition = edition
        self._age_rating = age_rating
        self._discount = discount

        # This will be some long code but it is what it is

        # Getters

    def get_title(self) -> str:
        return self._title

    def get_author(self) -> str:
        return self._author

    def get_genre(self) -> str:
        return self._genre

    def get_publish_year(self) -> int:
        return self._publish_year

    def get_publisher(self) -> str:
        return self._publisher

    def get_type(self) -> str:
        return self._type

    def get_price(self) -> int:
        return self._price

    def get_stock(self) -> int:
        return self._stock

    def get_ISBN(self) -> str:
        return self._ISBN

    def get_edition(self) -> str:
        return self._edition

    def get_age_rating(self) -> int:
        return self._age_rating

    def get_discount(self) -> int:
        return self._discount

    # Setters

    def set_stock(self, new_stock: int):
        self._stock = new_stock

    # Book functionality

    def set_discount(self, new_discount: int):
        self._discount = new_discount

    def _str_(self):
        return f'{self._title}: {self._author}'


class User:
    def _init_(self, username: str, password: str, email: str, number: int, FIN: str):
        self._username = username
        self._password = password
        self._email = email
        self._number = number
        self._FIN = FIN

    # Getter functions for user

    def get_username(self) -> str:
        return self._username

    def get_password(self) -> str:
        return self._password

    def get_email(self) -> str:
        return self._email

    def get_number(self) -> int:
        return self._number

    def get_FIN(self) -> str:
        return self._FIN

    # Setter functions in user

    def set_username(self, username: str):
        self._username = username

    def set_password(self, password: str):
        self._password = password

    def set_email(self, email: str):
        self._email = email

    def set_number(self, number: int):
        self._number = number


class Reader(User):
    # This class is for any casual user
    def _init_(self, wallet: int):
        self._borrowed_books: list[Book] = []
        self._wallet: int = wallet

    # Getters and Setters for reader

    def get_borrowed_books(self) -> list[dict]:
        return self._borrowed_books

    def get_wallet(self) -> int:
        return self._wallet

    def set_borrowed_books(self, current_borrowed: list[dict]):
        self._borrowed_books = current_borrowed

    def set_walltet(self, current_wallet: int):
        self._wallet = current_wallet

    # Reader functionality
    def track_books():
        pass

    def return_books(self, target_book: Book) -> list[Book]:
        pass


class Library:
    def _init_(self):
        self._white_list: list[Reader] = []
        self._black_list: list[Reader] = []
        self._books: list[Book] = []
        self._users: list[Reader] = []

    # Library functionality

    def find_user(self, target_user: User) -> User:
        for user in self._users:
            if user == target_user:
                return user
        return None

    def find_book(self, target_book: Book) -> Book:
        for book in self._books:
            if book == target_book:
                return book
        return None

    def append_blacklist(self, user: Reader):
        # This function will add users to a blacklist when overdue
        self._black_list.append(user)

    def add_book(self, book: Book):
        self._books.append(book)

    def view_book_list(self) -> list[Book]:
        return self._books


class Admin(User):

    def _init_(self, username: str, password: str, email: str, number: int, FIN: str, library: Library):
        super()._init_(username, password, email, number, FIN)
        self._library = library
    # Admins functionality

    def update_book(self, book: Book, new_price: int):
        book.set_price(new_price)

    def delete_book(self, book: Book):
        self._library._books.remove(book)


def main():
    pass
