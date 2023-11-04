"""Exercise 1 3"""

total = 0
with open("./Data/portfolio.dat", "r") as file:
    for line in file.readlines():
        data = line.split()
        total += int(data[1]) * float(data[2])
print(total)
