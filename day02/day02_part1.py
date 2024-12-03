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
        report_type = 1 # 0 - Unsafe, 1 - Safe
        prev_direction = report[1] > report[0]
        prev_level = report.pop(0)
        for level in report:
            gap = abs(level - prev_level)
            direction = level > prev_level
            prev_level = level

            if gap < 1 or gap > 3:
                report_type = 0
                break

            if direction != prev_direction:
                report_type = 0
                break

        safe_reports += report_type

    print("Safe reports:", safe_reports)

main()
