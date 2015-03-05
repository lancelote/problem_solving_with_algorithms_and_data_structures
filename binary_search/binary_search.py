def binary_search(lst, item):
    """
    O(log(n))
    """
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if lst[midpoint] == item:
            return True
        elif lst[midpoint] > item:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return found


def recursion_binary_search(lst, item, first=0, last=None):
    last = len(lst) - 1 if last is None else last
    midpoint = (first + last)//2
    if last - first < 0:
        return False
    elif lst[midpoint] == item:
        return True
    elif lst[midpoint] > item:
        return recursion_binary_search(lst, item, first, midpoint - 1)
    else:
        return recursion_binary_search(lst, item, midpoint + 1, last)