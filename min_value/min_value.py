def min_value_o_n2(lst):
    min_value = lst[0]
    for i in range(len(lst)):
        for j in range(1, len(lst)):
            if lst[i] > lst[j]:
                continue
            else:
                min_value = lst[i]
    return min_value


def min_value_o_n(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value


print(min_value_o_n2([2, 6, 5, 3, 9, 0, 1]))
print(min_value_o_n([2, 6, 5, 3, 9, 0, 1]))