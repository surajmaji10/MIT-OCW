
import random

def is_subset(L1, L2):
    """is L1 a subset of L2"""
    for l1 in L1:
        found = False
        for l2 in L2:
            if l2 == l1:
                found = True
                break
        if not found:
            return False
    return True


# n = 10
# L1 = [random.randint(0, 20) for i in range(n)]
# L2 = [random.randint(0, 20) for j in range(n//2)]
# print(is_subset(L2, L1))
#
# count = 100000
# success = 0
# for c in range(count):
#     n = 10
#     L1 = [random.randint(0, 20) for i in range(n)]
#     L2 = [random.randint(0, 20) for j in range(n // 2)]
#     success += is_subset(L2, L1)
# print(success/count)
#
# count = 100000
# success = 0
# for c in range(count):
#     n = 10
#     m = random.randint(1, n)
#     n = random.randint(1, n)
#     L1 = [random.randint(0, 20) for i in range(m)]
#     L2 = [random.randint(0, 20) for j in range(n)]
#     success += is_subset(L2, L1)
#     success += is_subset(L1, L2)
# print(success/count)


def intersection(L1, L2):
    L = []
    for l1 in L1:
        if l1 in L2:
            L2.remove(l1)
            L.append(l1)
    return L

n = 10
L1 = [random.randint(0, 20) for i in range(n)]
L2 = [random.randint(0, 20) for j in range(n)]
print(L1, L2)
print(intersection(L1, L2))
# print(intersection(L2, L1), intersection(L1, L2))

count = 100000
length = 0
for c in range(count):
    n = 100
    L1 = [random.randint(0, 20) for i in range(n)]
    L2 = [random.randint(0, 20) for j in range(n)]
    length += len(intersection(L1, L2))
print(length/count)


