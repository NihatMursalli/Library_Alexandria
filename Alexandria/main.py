class User:
    def __init__(self, username, password, email, number, FIN):
        self._username = username
        self._password = password
        self._email = email
        self._number = number
        self._FIN = FIN

    # Getter functions for user

    def get_username(self):
        return self._username
    
    def get_password(self):
        return self._password
    
    def get_email(self):
        return self._email
    
    def get_number(self):
        return self._number
    
    def get_FIN(self):
        return self._FIN
    
    # Setter functions in user

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_email(self, email):
        self._email = email

    def set_number(self, number):
        self._number = number



class Admin(User):
    def __init__():
        pass

    # Admins functionality
    def append_blacklist():
        # This function will add users to a blacklist when overdue
        pass

    def add_book():
        pass

    def update_book():
        pass

    def delete_book():
        pass

class Reader(User):
    # This class is for any casual user
    def __init__(self, wallet):
        self._borrowed_books = []
        self._wallet = wallet

    # Getters and Setters for reader

    def get_borrowed_books(self):
        return self._borrowed_books
    
    def get_wallet(self):
        return self._wallet
    
    def set_borrowed_books(self, current_amount):
        self._borrowed_books = current_amount
    
    def set_walltet(self, current_wallet):
        self._wallet = current_wallet

    # Reader functionality
    def view_book_list():
        pass

    def track_books():
        pass

    def return_books():
        pass

class Book_class:
    # This classes name is self-explanitory
    def __init__(self, title, author,
                 genre, publish_year,
                 publisher, type, price,
                 stock, ISBN, edition,
                 age_rating):
        
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

        # This will be some long code but it is what it is

        # Getters

    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author
    
    def get_genre(self):
        return self._genre
    
    def get_publish_year(self):
        return self._publish_year
    
    def get_publisher(self):
        return self._publisher
    
    def get_type(self):
        return self._type
    
    def get_price(self):
        return self._price
    
    def get_stock(self):
        return self._stock
    
    def get_ISBN(self):
        return self._ISBN
    
    def get_edition(self):
        return self._edition
    
    def get_age_rating(self):
        return self._age_rating
    
    # Setters

    def set_stock(self, new_stock):
        self._stock = new_stock

    # Book functionality

    def set_discount(self, discount_percent):
        orig_price = self.get_price()
        self._price = (orig_price//100)*discount_percent
        

def main():
    pass