"""
reader.py exercise 5.3
"""
import csv


def convert_csv(lines, func, *, headers=None):
    lines = csv.reader(lines)
    data = []
    if headers is None:
        headers = next(lines)
    for line in lines:
        data.append(func(headers, line))
    return data
    

def read_csv_as_dicts(filename, coltypes, *, headers=None):
    """csv data to list of dicts"""
    f = open(filename)
    return csv_as_dicts(f, coltypes, headers=headers)


def csv_as_dicts(lines, types, *, headers=None):
    """csv lines to list of dicts"""
    data = convert_csv(lines, lambda headers, x: {name: func(
        val) for name, func, val in zip(headers, types, x)})
    return data


def csv_as_instances(lines, cls, *, headers=None):
    """csv lines into a list of instances"""
    data = convert_csv(lines, lambda headers, row: cls.from_row(row))
    return data


def read_csv_as_instances(filename, cls, *, headers=None):
    """csv data into a list of instances"""
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)
