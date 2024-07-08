## bubble sort algo
def cmp(x, y):
    return x < y


def bubble_sort(ls, cmp=lambda x,y: x<=y):
    i = 0
    n = len(ls)
    swapped = False
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if cmp(ls[j], ls[j+1]):
                swapped = True
                t = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = t
        if not swapped:
            break
    return ls


ls = [1, 10, 2, 9, 3, 7, 4, 6, 5, 8]
print(bubble_sort(ls, cmp))

