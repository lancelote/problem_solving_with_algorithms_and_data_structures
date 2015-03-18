import itertools


def anagram_1(s1, s2):
    lst = list(s2)
    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False

        while pos2 < len(s2) and not found:
            if s1[pos1] == s2[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            lst[pos1] = None
        else:
            still_ok = False

        pos1 += 1
    return still_ok


def anagram_2(s1, s2):
    lst1 = list(s1)
    lst2 = list(s2)

    lst1.sort()
    lst2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if lst1[pos] == lst2[pos]:
            pos += 1
        else:
            matches = False

    return matches


def anagram_3(s1, s2):
    matches = True
    permutations = [''.join(i) for i in itertools.permutations(s1)]

    if s2 not in permutations:
        matches = False

    return matches