"""Exercise 3 3"""
import csv


def read_csv_as_dicts(filename, coltypes):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    data = []
    for row in rows:
        data.append({name: func(val)
                    for name, func, val in zip(headers, coltypes, row)})
    return data

def read_csv_as_instances(filename, cls):
    """Read a CSV file into a list of instances"""
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
