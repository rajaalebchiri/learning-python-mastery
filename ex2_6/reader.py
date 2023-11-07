# reader.py
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
