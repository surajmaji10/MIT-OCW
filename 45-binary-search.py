import random

def binary_search(L, e):
    start = 0
    end = len(L) - 1
    while start <= end:
        mid = (start + end)//2
        if L[mid] == e:
            return mid
        elif L[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# L = [random.randint(0, 1000) for i in range(1000000)]
# L.sort()
# e = random.choice(L)
#
# idx = binary_search(L, e)
# print(L)
# print(idx, L[idx])


def int_to_str(i):
    if i == 0:
        return '0'
    neg = False
    digits = '0123456789'
    if i < 0:
        neg = True
        i = -i
    result = ''
    while i > 0:
        r = i % 10
        i = i // 10
        c = digits[r]
        result = c + result
    return result if not neg else '-'+result

n = random.randint(0, 10000000000000)
if n % 2 == 0:
    n *= -1
print(n, int_to_str(n))




