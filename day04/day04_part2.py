import re


def main():
    data = open("data.txt")
    v_lines = []
    for line in data:
        v_lines.append(line.strip())
    data.close()

    dtl_lines = to_diagonal_tl(v_lines)

    count = 0
    for dtl_line_ix, dtl_line in enumerate(dtl_lines):
        count += has_cross_with(r"(?=(MAS))", dtl_line, dtl_line_ix, v_lines)
        count += has_cross_with(r"(?=(SAM))", dtl_line, dtl_line_ix, v_lines)

    print("XMAS count:", count)


def has_cross_with(pattern, dtl_line, dtl_line_ix, v_lines):
    count = 0
    diagonal_y = max(0, -1 * dtl_line_ix + len(v_lines) - 1)
    diagonal_x = abs(min(0, -1 * dtl_line_ix + len(v_lines) - 1))

    dtl_matches = re.finditer(pattern, dtl_line)
    for dtl_match in dtl_matches:
        y = diagonal_y + dtl_match.start()
        x = diagonal_x + dtl_match.start() + 2

        phrase_on_other_diagonal = v_lines[y][x] + v_lines[y + 1][x - 1] + v_lines[y + 2][x - 2]
        if phrase_on_other_diagonal == "SAM" or phrase_on_other_diagonal == "MAS":
            count += 1
    return count


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


main()
