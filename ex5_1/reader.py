"""
reader.py exercise 5.1
"""
import csv


def read_csv_as_dicts(filename, coltypes, *, headers=None):
    """csv data to list of dicts"""
    f = open(filename)
    return csv_as_dicts(f, coltypes, headers=headers)


def csv_as_dicts(lines, types, *, headers=None):
    """csv lines to list of dicts"""
    data = []
    lines = csv.reader(lines)
    if headers is None:
        headers = next(lines)
    for line in lines:
        data.append({name: func(val)
                    for name, func, val in zip(headers, types, line)})
    return data


def csv_as_instances(lines, cls, *, headers=None):
    """csv lines into a list of instances"""
    data = []
    lines = csv.reader(lines)
    if headers is None:
        headers = next(lines)
    for line in lines:
        record = cls.from_row(line)
        data.append(record)
    return data


def read_csv_as_instances(filename, cls, *, headers=None):
    """csv data into a list of instances"""
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)
