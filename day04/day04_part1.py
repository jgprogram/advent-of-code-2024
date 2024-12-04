import re


def main():
    data = open("data.txt")
    v_lines = []
    for line in data:
        v_lines.append(line.strip())
    data.close()
    h_lines = to_columns(v_lines)
    dtl_lines = to_diagonal_tl(v_lines)
    dtr_lines = to_diagonal_tl(reverse_lines(v_lines))

    count = find_xmas_cnt(v_lines)
    count += find_xmas_cnt(h_lines)
    count += find_xmas_cnt(dtl_lines)
    count += find_xmas_cnt(dtr_lines)

    print("XMAS count:", count)


def find_xmas_cnt(data_lines):
    cnt = 0
    for line in data_lines:
        cnt += len(re.findall(r"(?=(XMAS))", line))
        cnt += len(re.findall(r"(?=(XMAS))", line[::-1]))

    print("Found:", cnt)
    return cnt


def to_columns(data_lines):
    columns = []
    row_ixs = len(data_lines)
    col_ixs = len(data_lines[0])

    for col_ix in range(col_ixs):
        column = ""
        for row_ix in range(row_ixs):
            column += data_lines[row_ix][col_ix]
        columns.append(column)

    return columns


def to_diagonal_tl(data_lines):
    diagonals = []
    row_ixs = len(data_lines) - 1
    col_ixs = len(data_lines[0]) - 1

    start_col = 0
    start_row = row_ixs

    while start_row >= 0 or start_col < col_ixs:
        diagonal = ""

        col_ix = start_col
        for row_ix in range(max(0, start_row), row_ixs + 1):
            diagonal += data_lines[row_ix][col_ix]

            col_ix += 1
            if col_ix > col_ixs:
                break

        if diagonal != "":
            diagonals.append(diagonal)

        start_row -= 1
        if start_row < 0:
            start_col += 1

    return diagonals


def reverse_lines(data_lines):
    reversed_lines = []
    for line in data_lines:
        reversed_lines.append(line[::-1])
    return reversed_lines


main()
