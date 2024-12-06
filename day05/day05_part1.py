import re
import math


def main():
    data = open("data.txt")

    rules = {}
    updates = []
    for data_line in data:
        if data_line.strip() == "":
            break

        numbers = re.findall(r"\d+", data_line)
        if numbers[1] not in rules:
            rules[numbers[1]] = [int(numbers[0])]
        else:
            rules[numbers[1]].append(int(numbers[0]))

    for data_line in data:
        updates.append(list(map(int, re.findall(r"\d+", data_line))))

    first_key = next(iter(rules))
    print("First rule:", first_key, ":", rules[first_key], "First update:", updates[0])
    data.close()

    total = 0
    for update in updates:
        is_valid = True
        for ix, val in enumerate(update):
            if ix + 1 == len(update):
                break

            for next_ix in range(ix + 1, len(update)):
                if str(val) in rules and update[next_ix] in rules[str(val)]:
                    is_valid = False
                    break
            if not is_valid:
                break

        if is_valid:
            total += update[math.floor(len(update) / 2)]

    print(total)


main()
