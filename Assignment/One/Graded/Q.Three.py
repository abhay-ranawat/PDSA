l = [1, 2, 3, -4, 3, 2, 1, 5, -6, 7, 8, 9, 10]
p = 6


def find_Min_Difference(l, p):
    min_diff = 99999

    l = sorted(l)

    for i in range(len(l)):
        tl = l[i:i+p]

        if (len(tl) == p):
            if ((tl[-1] - tl[0]) < min_diff):
                min_diff = (tl[-1] - tl[0])

    return (min_diff)


print(find_Min_Difference(l, p))
