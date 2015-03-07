def gap_insertion_sort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):
        current_value = lst[i]
        pos = i

        while pos >= gap and lst[pos - gap] > current_value:
            lst[pos] = lst[pos - gap]
            pos -= gap

        lst[pos] = current_value


def shell_sort(lst):
    gap = len(lst)//2

    while gap > 0:
        for start in range(gap):
            gap_insertion_sort(lst, start, gap)
        gap //= 2