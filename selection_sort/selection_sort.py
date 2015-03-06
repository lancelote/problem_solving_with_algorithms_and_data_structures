def selection_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        max_position = 0
        for j in range(1, i + 1):
            if lst[j] > lst[max_position]:
                max_position = j

        lst[i], lst[max_position] = lst[max_position], lst[i]