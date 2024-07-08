# merge sort => n.logn time

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


print(mergesort(["Akash", "Suraj", "Anup", "Mithu"]))
print(mergesort([1, 4, 2, 3, 7, 5, 10, 12, 8, 9]))
print(mergesort([1.1, 4.2, 2.3, 3.9, 7.6, 5.01, 10.00, 12.0, 8.0, 9]))


