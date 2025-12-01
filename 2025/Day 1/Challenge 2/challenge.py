password = 0
value = 50

with open("input.txt", "r") as input:
    for line in input:
        if line[0] == "L":
            value = -value % 100
            value = value + int(line[1:])
            password += value // 100
            value = value % 100
            value = -value
        else:
            value = value % 100
            value = value + int(line[1:])
            password += value // 100
    print(password)