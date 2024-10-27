

def gen_ss(L):
    if len(L) == 0:
        return [[]]
    smaller = gen_ss(L[:-1])
    last = L[-1]
    bigger = []
    for small in smaller:
        big = small[:]
        big.append(last)
        bigger.append(big)
    # print(L, smaller, bigger)
    smaller.extend(bigger)
    return smaller

def gen_ss2(L):
    if len(L) == 0:
        return [[]]
    smaller = gen_ss(L[:-1])
    last = L[-1]
    bigger = []
    for small in smaller:
        bigger.append(small + [last])
    return smaller + bigger

# print(gen_ss([1, 2, 3]))
# print(gen_ss2([1, 2, 3]))

ls = [i for i in range(20)]
print(gen_ss(ls))