class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        if not value.strip():
            raise Exception("Name cannot be empty.")
        self._name = value

    # returns all contracts of this author
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    # returns all books of this author via contracts
    def books(self):
        return [contract.book for contract in self.contracts()]

    # creates and returns a new contract
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # total royalties earned
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    # title property
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string.")
        if not value.strip():
            raise Exception("Title cannot be empty.")
        self._title = value

    # returns all contracts for this book
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    # returns all authors who have contracts for this book
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # author property
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author.")
        self._author = value

    # book property
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of Book.")
        self._book = value

    # date property
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string.")
        if not value.strip():
            raise Exception("Date cannot be empty.")
        self._date = value

    # royalties property
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer.")
        if value < 0:
            raise Exception("Royalties cannot be negative.")
        self._royalties = value

    # class method to return all contracts by date
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
