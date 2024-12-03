def main():
    data = open("data_tst.txt")
    left_list = []
    right_list = []
    for line in data:
        str_vals = line.split("  ")
        int_vals = []
        for str_val in str_vals:
            int_vals.append(int(str_val))
        left_list.append(int_vals[0])
        right_list.append(int_vals[1])

    data.close()

    print("First row: [", left_list[0], ",", right_list[0], "]", sep="")

    total_distance = 0
    entries_left = len(left_list)

    while entries_left > 0:
        left_min = find_min_with_index(left_list)
        right_min = find_min_with_index(right_list)
        left_list.pop(left_min[0])
        right_list.pop(right_min[0])
        entries_left = len(left_list)
        #print("Found mins:", left_min, right_min)
        total_distance += abs(left_min[1] - right_min[1])


    print("Total distance:", total_distance)


def find_min_with_index(data):
    min_ix = 0
    min_entry = data[0]
    for i, entry in enumerate(data):
        if entry < min_entry:
            min_entry = entry
            min_ix = i
    return [min_ix, min_entry]

main()
