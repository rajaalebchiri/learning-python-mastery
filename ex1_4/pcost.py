"""Exercise 1 4"""

def portfolio_cost(filename):
    total = 0
    with open(filename, "r") as file:
        for line in file.readlines():
            data = line.split()
            try:
                total += int(data[1]) * float(data[2])
            except ValueError as error:
                print("Couldn't parse:", repr(line))
                print("Readon:", error)
    return total

print(portfolio_cost("Data/portfolio3.dat"))