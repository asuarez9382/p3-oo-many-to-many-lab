class Author:

    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception

    def contracts(self):
        return [ contract for contract in Contract.all if contract.author == self ]

    def books(self):
        contracts = [ contract for contract in Contract.all if contract.author == self ]
        return [ contract.book for contract in contracts ]


    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)


    def total_royalties(self):
        sum = 0
        contracts = self.contracts()
        for contract in contracts:
            sum += contract.royalties
        return sum

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        self.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise Execption


    def contracts(self):
        return [ contract for contract in Contract.all if contract.book == self ]


    def authors(self):
        contracts = [ contract for contract in Contract.all if contract.book == self ]
        return [ contract.author for contract in contracts ]


class Contract:

    all =[]

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Execption

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Execption

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception

    @classmethod
    def contracts_by_date(cls, date):
        return [ contract for contract in cls.all if contract.date == date ]
