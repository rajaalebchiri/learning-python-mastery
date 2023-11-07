# readrides_tuples.py
import csv
import collections.abc

class RideData(collections.abc.Sequence):
    """RideData"""
    def __init__(self):
        """Each value is a list with all of the values (a column)"""
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # all lists assumed to have the same length
        return len(self.routes)
    
    def __getitem__(self, index):
        return {
            'route': self.routes[index],
            'date': self.dates[index],
            'daytype': self.daytypes[index],
            'rides': self.numrides[index]
        }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

def read_rides_as_tuples(filename):
    """
    Read the bus data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dictionary(filename):
    """
    Read the bus data as a dictionary
    """
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class(filename):
    """
    Read the bus data as a dictionary
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route=route, date=date, daytype=daytype, rides=rides)
            records.append(record)
    return records


def read_rides_as_columns(filename):
    """
    Read the bus ride data into 4 lists, representing columns
    """
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)




if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows_tuples = read_rides_as_class("Data/ctabus.csv")
    print("Memory Use For A Tuple: Current %d, Peak %d" %
          tracemalloc.get_traced_memory())
    tracemalloc.stop()
