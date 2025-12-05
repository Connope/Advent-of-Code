def which_battery(bank, remaining_needed):
    battery = max([int(x) for x in bank[:-remaining_needed]])
    index_battery = bank.index(str(battery))
    remaining_bank = bank[index_battery+1:]
    return remaining_bank, battery

joltage = 0

with open("input.txt", "r") as input:
    for bank in input.readlines():
        values = list(bank)[:-1]
        this_joltage = ""
        for remaining_needed in range(12, 0, -1):
            bank, battery = which_battery(bank, remaining_needed)
            this_joltage += str(battery)
        joltage += int(this_joltage)

print(joltage)