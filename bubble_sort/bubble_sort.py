def bubble_sort(lst):
    exchanges = True
    pass_num = len(lst) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                exchanges = True
        pass_num -= 1