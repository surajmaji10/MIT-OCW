# merge sort and merge algorithm (recursive DnC)
def merge(xs, ys, cmp=lambda x, y: x <= y):
    i = 0
    j = 0
    m = len(xs)
    n = len(ys)
    zs = []

    while i < m and j < n:
        if cmp(xs[i], ys[j]):
            zs.append(xs[i])
            i += 1
        else:
            zs.append(ys[j])
            j += 1

    while i < m:
        zs.append(xs[i])
        i += 1
    while j < n:
        zs.append(ys[j])
        j += 1

    return zs


def mergesort(ls, cmp=lambda x, y: x <= y):
    if len(ls) <= 1:
        return ls[:]
    m = len(ls) // 2
    xs = mergesort(ls[:m], cmp)
    ys = mergesort(ls[m:], cmp)
    zs = merge(xs, ys, cmp)
    return zs


# print(mergesort(["Akash", "Suraj", "Anup", "Mithu"]))
# print(mergesort([1, 4, 2, 3, 7, 5, 10, 12, 8, 9]))
# print(mergesort([1.1, 4.2, 2.3, 3.9, 7.6, 5.01, 10.00, 12.0, 8.0, 9]))


# custom comparators
def cmp_first_last(name1, name2):
    name1 = name1.split()
    name2 = name2.split()
    if name1[0] != name2[0]:
        return name1[0] <= name2[0]
    else:
        return name1[1] <= name2[1]


def cmp_last_first(name1, name2):
    name1 = name1.split()
    name2 = name2.split()
    if name1[1] != name2[1]:
        return name1[1] <= name2[1]
    else:
        return name1[0] <= name2[0]


ls = [
    "Akash Maji",
    "Anup Maji",
    "Akash Mali",
    "Suraj Jali",
    "Suraj Pali",
    "Mithu Bali",
    "Situ Kali",
]

print(mergesort(ls, cmp_first_last))
print(mergesort(ls, cmp_last_first))

