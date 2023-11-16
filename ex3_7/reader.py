"""Exercise 3 7"""
import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return {name: func(val) for name, func, val in zip(headers, self.types, row)}

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)

def read_csv_as_dicts(filename, coltypes):
    dict_class = DictCSVParser(types=coltypes)
    return dict_class.parse(filename=filename)

def read_csv_as_instances(filename, cls):
    """Read a CSV file into a list of instances"""
    instance = InstanceCSVParser(cls=cls)
    return instance.parse(filename=filename)
