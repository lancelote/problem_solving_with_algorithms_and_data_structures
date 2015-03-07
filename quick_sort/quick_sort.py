def partition(lst, first, last):
    pivot_value = lst[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and lst[left_mark] <= pivot_value:
            left_mark += 1

        while right_mark >= left_mark and lst[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            lst[left_mark], lst[right_mark] = lst[right_mark], lst[left_mark]

    lst[first], lst[right_mark] = lst[right_mark], lst[first]

    return right_mark


def quick_sort_help(lst, first, last):
    if first < last:
        split_point = partition(lst, first, last)
        quick_sort_help(lst, first, split_point - 1)
        quick_sort_help(lst, split_point + 1, last)


def quick_sort(lst):
    quick_sort_help(lst, 0, len(lst) - 1)