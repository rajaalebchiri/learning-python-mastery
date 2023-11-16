"""Table Formatting"""

class TableFormatter:
    """Formatting Class"""
    def headings(self, headers):
        raise NotImplementedError()

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
    formatter.headings(fields)
    for r in data:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
