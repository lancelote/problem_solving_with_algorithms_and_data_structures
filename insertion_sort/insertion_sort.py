def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_value = lst[i]
        position = i

        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position -= 1

        lst[position] = current_value