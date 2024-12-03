def main():
    data = open("data.txt")
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

    similarity_score = 0

    for l_entry in left_list:
        r_entries_cnt = 0
        for r_entry in right_list:
            if l_entry == r_entry:
                r_entries_cnt += 1
        similarity_score += l_entry * r_entries_cnt


    print("Similarity score:", similarity_score)

main()
