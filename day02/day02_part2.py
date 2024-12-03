def main():
    data_lines = open("data.txt")
    reports = []
    for line in data_lines:
        levels = []
        for entry in line.split(" "):
            levels.append(int(entry))
        reports.append(levels)

    print("First report:", reports[0])

    safe_reports = 0
    for report in reports:
        report_type = check_report_type(report)
        safe_reports += report_type

    print("Safe reports:", safe_reports)


def check_report_type(report, recurr = True):
    report_type = 1  # 0 - Unsafe, 1 - Safe
    prev_direction = None
    prev_level = report[0]
    for level in report[1:]:
        gap = abs(level - prev_level)
        direction = level > prev_level

        if gap < 1 or gap > 3 or (prev_direction is not None and direction != prev_direction):
            report_type = 0
            break
        else:
            prev_direction = direction
            prev_level = level

    if report_type == 0 and recurr:
        for ix in range(len(report)):
            if check_report_type(report[:ix] + report[ix + 1:], recurr=False) == 1:
                return 1

    return report_type

main()

