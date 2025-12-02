sum = 0

with open("input.txt", "r") as input:
    for id_range in input.read().split(","):
        min, max = id_range.split("-")
        if len(min) == len(max) and len(min) % 2 == 1:
            continue
        else:
            for id in range(int(min), int(max) + 1):
                length = len(str(id))
                if length % 2 == 1:
                    continue
                else:
                    invalid = True
                    for i in range(0, int(length / 2)):
                        if str(id)[i] == str(id)[i + int(length / 2)]:
                            continue
                        else:
                            invalid = False
                    if invalid:
                        sum += id
                    
    print(sum)