joltage = 0

with open("input.txt", "r") as input:
    for bank in input.readlines():
        values = list(bank)[:-1]
        tens = max([int(x) for x in values[:-1]])
        index_first = values.index(str(tens))
        units = max([int(x) for x in values[index_first+1:]])
        joltage += 10 * tens + units

print(joltage)