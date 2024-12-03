import re

def main():
    data_lines = open("data.txt")

    total = 0
    for data in data_lines:
        matches = re.findall(r'mul\(\d+,\d+\)', data)
        for match in matches:
            numbers = re.findall(r'\d+', match)
            total += int(numbers[0]) * int(numbers[1])
        print(matches)

    print(total)
main()
