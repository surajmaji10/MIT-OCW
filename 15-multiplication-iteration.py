# a iterative program

m = int(input("Enter num1: "))
n = int(input("Enter num2: "))

def iter_mult(m, n):
    if n == 0 or m == 0:
        return 0

    tot = 0
    if n < 0:
        while n < 0:
            tot += m
            n += 1
        return -tot
    else:
        while n > 0:
            tot += m
            n -= 1
        return tot

print("{} * {} = {}".format(m, n, iter_mult(m, n)))


