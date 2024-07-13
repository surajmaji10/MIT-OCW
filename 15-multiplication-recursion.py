# this is a sample code from MIT OCW 18.00
# a recursive program

m = int(input("Enter num1: "))
n = int(input("Enter num2: "))

def mult(m, n):
    if n == 0:
        return 0
    elif n > 0:
        return m + mult(m, n-1)
    else:
        return -m + mult(m, n+1)

ans = mult(m, n)
print("{} * {} = {}".format(m, n, ans))
