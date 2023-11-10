"""Exercise 3 1"""
import csv

class Stock:
    """Stock object"""
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

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
        stock = Stock(row[0], int(row[1]), float(row[2]))
        data_portfolio.append(stock)
    return data_portfolio

def print_portfolio(data):
    """Print the portfolio data"""
    print("%10s %10s %10s" % ("name", "shares", "price"))
    #print("%10s %10s %10s" % ("-" * 10, "-" * 10, "-" * 10))
    print(('-'*10 + ' ') * 3)
    for s in data:
        print("%10s %10d %10.2f" % (s.name, s.shares, s.price))
