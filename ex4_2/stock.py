"""Exercise 4 2"""
import csv

class Stock:
    """Stock object"""
    __slots__ = ("name", "_shares", "_price")
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    
    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, amount):
        self.shares -= amount

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1].__name__}")
        if value < 0:
            raise ValueError("hares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected {self._types[2].__name__}")
        if value < 0:
            raise ValueError("hares must be >= 0")
        self._price = value
    

def read_portfolio(filename):
    """array of stock objects"""
    data_portfolio = []
    file = open(filename)
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        stock = Stock.from_row(row)
        data_portfolio.append(stock)
    return data_portfolio

