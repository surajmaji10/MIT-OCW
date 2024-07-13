# this is a sample code from MIT OCW 18.00

# TC => BigOh (n*n)
## selection sort

def cmp(x, y):
    return x >= y

# default is ASC order
def sel_sort(ls, cmp=lambda x,y: x<y):
    n = len(ls)

    for i in range(0, n-1):
        min_idx = i
        min_val = ls[i]
        j = i + 1
        while j < n:
            # if ls[j] < min_val:
            if cmp(ls[j], min_val):
                min_idx = j
                min_val = ls[j]
            j += 1
        t = ls[i]
        ls[i] = ls[min_idx]
        ls[min_idx] = t
        print("Intermediate List: {}".format(ls))

    return ls


ls = [10, 4, 2, 3, 7, 6, 5, 1, 9, 8]
print(sel_sort(ls))
print(sel_sort(ls, cmp))

