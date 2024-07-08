## factorial(n) = n * (n-1) * (n-2) * ... * 3 * 2 * 1 = n!
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

num = int(input("Enter a number: "))
ans = fact(num)
print("{}! = {}".format(num, ans))

