r1, c1, r2, c2 = [int(x) for x in input().split()]

def ladia(r1, c1, r2, c2):
    if r1 == r2 or c1 == c2:
        return 1
    else:
        return 2


def slon(r1, c1, r2, c2):
    if (r1 + c1) %2 != (r2 + c2) %2:
        return 0
    elif abs(r1 -r2) == abs(c1-c2):
        return 1
    else:
        return 2


def king(r1, c1, r2, c2):
    return max(abs(r1-r2), abs(c1-c2))


print(ladia(r1, c1, r2, c2), slon(r1, c1, r2, c2), king(r1, c1, r2, c2))
