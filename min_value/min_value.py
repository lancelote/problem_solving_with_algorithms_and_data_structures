def min_value_o_n2(lst):
    min_value = lst[0]
    for i in lst:
        is_min = True
        for j in lst:
            if i > j:
                is_min = False
        if is_min:
            min_value = i
    return min_value


def min_value_o_n(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value