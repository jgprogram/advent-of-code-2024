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
        to_count = False
        sorted_update = update[::]
        is_sorted = False

        while not is_sorted:
            for ix, val in enumerate(sorted_update):
                if ix + 1 == len(sorted_update):
                    is_sorted = True
                    break

                valid = True
                for next_ix in range(ix + 1, len(sorted_update)):
                    if str(val) in rules and sorted_update[next_ix] in rules[str(val)]:
                        to_count = True
                        valid = False
                        element = sorted_update.pop(next_ix)
                        sorted_update.insert(ix, element)

                if not valid:
                    break

        if to_count:
            total += sorted_update[math.floor(len(sorted_update) / 2)]

    print(total)


main()
