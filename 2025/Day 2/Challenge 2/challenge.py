def check_id_invalid(id, pattern_length):
    length = len(str(id))
    if length % pattern_length != 0:
        return False
    else:
        invalid = True
        for j in range(1, int(length / pattern_length)):
            for i in range(0, pattern_length):
                if str(id)[i] == str(id)[i + j * pattern_length]:
                    continue
                else:
                    invalid = False
        if invalid:
            return invalid
    return False

sum = 0


with open("input.txt", "r") as input:
    for id_range in input.read().split(","):
        min, max = id_range.split("-")
        for id in range(int(min), int(max) + 1):
            invalid = False
            for pattern_length in range(1, len(str(id))):
                if not invalid:
                    if check_id_invalid(id, pattern_length):
                        sum += id
                        invalid = True
                        continue
    print(sum)

