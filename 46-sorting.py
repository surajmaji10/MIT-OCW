import random

def monkey_sort(L):
    def is_sorted(L):
        for i in range(1, len(L)):
            if L[i] < L[i-1]:
                return False
        return True
    while not is_sorted(L):
        random.shuffle(L)

# L = [random.randint(0, 100) for i in range(10)]
# print(L)
# monkey_sort(L)
# print(L)

def bubble_sort(L):
    while True:
        swap = False
        for i in range(1, len(L)):
            if L[i] < L[i-1]:
                L[i], L[i-1] = L[i-1], L[i]
                swap = True
        if not swap:
            break
    return

L = [random.randint(0, 100) for i in range(10)]
print(L)
bubble_sort(L)
print(L)

def bubble_sort2(L):
    n = len(L)
    for i in range(n-1):
        swap = False
        for j in range(n-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                swap = True
        if not swap:
            break
    return

L = [random.randint(0, 100) for i in range(10)]
print(L)
bubble_sort2(L)
print(L)


def selection_sort(L):
    suffix_start = 0
    while suffix_start != len(L):
        for i in range(suffix_start, len(L)):
            if L[i] < L[suffix_start]:
                L[i], L[suffix_start] = L[suffix_start], L[i]
        suffix_start += 1
    return

L = [random.randint(0, 100) for i in range(10)]
print(L)
selection_sort(L)
print(L)

def selection_sort2(L):
    n = len(L)
    for i in range(0, n-1):
        mini = i
        for j in range(i+1, n):
            if L[j] < L[mini]:
                mini = j
        if mini != i:
            L[i], L[mini] = L[mini], L[i]
    return

L = [random.randint(0, 100) for i in range(10)]
print(L)
selection_sort2(L)
print(L)

def merge_sort(L):
    def merge(left, right):
        i, j = 0, 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

    def sort(L):
        if len(L) < 2:
            return L[:]
        mid = len(L) // 2
        left = sort(L[:mid])
        right = sort(L[mid:])
        return merge(left, right)

    return sort(L)

L = [random.randint(0, 100) for i in range(10)]
print(L)
merge_sort(L)
print(L)
