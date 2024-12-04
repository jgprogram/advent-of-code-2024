import re


def main():
    data_lines = open("data.txt")

    total = 0
    enabled = True
    for data in data_lines:
        matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)

        for match in matches:
            if match == "do()":
                enabled = True
            elif match == "don't()":
                enabled = False
            elif enabled:
                numbers = re.findall(r'\d+', match)
                total += int(numbers[0]) * int(numbers[1])

    print(total)
    data_lines.close()


main()
