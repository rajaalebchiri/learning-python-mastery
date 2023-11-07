"""Data analysis challenge"""

import readrides

rows = readrides.read_rides_as_dictionary('Data/ctabus.csv')

# Question 1
bus_routes_chicago = {s['route'] for s in rows}

print("How many bus routes exist in Chicago?", len(bus_routes_chicago))

print("--------------------------------")

# Question 2
by_route_date = {}
for row in rows:
    by_route_date[row['route'], row['date']] = row['rides']

print("How many people rode the number 22 bus on February 2, 2011?", by_route_date["22", "02/02/2011"])

print("--------------------------------")

# Question 3

by_route = {}
for s in bus_routes_chicago:
    by_route[s] = 0
for row in rows:
    by_route[row["route"]] = by_route[row["route"]] + row["rides"]
    
print("Total Number of rides taken on each bus route")
for key, value in by_route.items():
    print(f"Route {key}: {value}")

# or
from collections import Counter
by_route_counter = Counter()
for s in rows:
    by_route_counter[s["route"]] += s["rides"]

for route, rides in by_route_counter.most_common():
    print(route, rides)

print("--------------------------------")

# Question 4: What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
from collections import defaultdict
route_dict = defaultdict(Counter)
for row in rows:
    year = row["date"].split("/")[2]
    route_dict[year][row["route"]] += row["rides"]
diffs = route_dict['2011'] - route_dict['2001']
for route, diff in diffs.most_common(5):
    print(route, diff)
