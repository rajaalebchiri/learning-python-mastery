"""Exercise 3 3"""
import csv

class Stock:
    """Stock object"""
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount


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


if __name__ == '__main__':
    import tableformat
    import reader
    portfolio = read_portfolio('Data/portfolio.csv')
    tableformat.print_table(portfolio, ['name', 'shares', 'price'])
