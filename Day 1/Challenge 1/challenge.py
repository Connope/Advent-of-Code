password = 0
value = 50

with open("input.txt", "r") as input:
    for line in input:
        if line[0] == "L":
            value -= int(line[1:])
            if value % 100 == 0:
                password += 1
        else:
            value += int(line[1:])
            if value % 100 == 0:
                password += 1
    print(password)