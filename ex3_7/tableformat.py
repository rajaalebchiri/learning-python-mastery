"""Table Formatting"""
import sys
from abc import ABC, abstractmethod

class TableFormatter(ABC):
    """Formatting Class"""

    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    """Text Table Formatter"""
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    """CSV Table Formatter"""
    def headings(self, headers):
        print(','.join(h for h in headers))

    def row(self, rowdata):
        print(",".join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    """HTML Table Formatter"""
    def headings(self, headers):
        print("<tr> " + ''.join(f"<th>{h}</th>" for h in headers) + " </tr>")
    
    def row(self, rowdata):
        print("<tr> " + ''.join(f"<td>{r}</td>" for r in rowdata) + " </tr>")


class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout

def create_formatter(type):
    """Formatter Creator"""
    if type in ('text', 'html', 'csv'):
        if type == 'text':
            return TextTableFormatter()
        elif type == 'html':
            return HTMLTableFormatter()
        else:
            return CSVTableFormatter()
    else:
        raise RuntimeError("Unknown type %s" % type)

def print_table(data, fields, formatter):
    """formatting a table"""
    if isinstance(formatter, TableFormatter):
        formatter.headings(fields)
        for r in data:
            rowdata = [getattr(r, fieldname) for fieldname in fields]
            formatter.row(rowdata)
    else:
        raise TypeError("Expected a TableFormatter")