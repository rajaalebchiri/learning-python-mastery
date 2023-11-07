# readport.py

import csv


def read_portfolio(filename):
    """
    A function that reads a file into a list of dicts
    """
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio
