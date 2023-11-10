"""Table Formatting"""

def print_table(data, attributes):
    """formatting a table"""
    number_fields = len(attributes)
    print(("%10s" * number_fields) % tuple(attributes))
    print(('-'*10 + ' ') * number_fields)
    for s in data:
        print(("%10s" * number_fields) % tuple([getattr(s, value) for value in attributes]))
