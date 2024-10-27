
import random

def linear_search(L, e):
    """search for e in L"""
    for l in L:
        if l == e:
            return True
    return False

def linear_search2(L, e):
    """search for e in L"""
    found = False
    for l in L:
        if l == e:
            found = True
    return found

n = 100
L = [random.randint(0, 1000) for i in range(n)]
e = random.choice(L)
print("L={0} \ncontains e={1} ?\n".format(L, e),linear_search(L, e))
e = random.choice(L)
print("L={0} \ncontains e={1} ?\n".format(L, e),linear_search2(L, e))