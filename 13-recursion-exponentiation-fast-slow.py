
# Find a power n (a^n in python without using **)
def exponentiate(a, n):
    """
    find a power n
    :param a: base (int)
    :param n: power (int)
    :return: base ** power (int)
    """
    if n == 0:
        return 1
    else:
        # subans = exponentiate(a, n-1)
        # ans = a * subans
        # return ans
        return a * exponentiate(a, n-1)

base = int(input("Enter base(a): "))
power = int(input("Enter power(n): "))
ans = exponentiate(base, power)
print("Slow {}^{}={}".format(base, power, ans))


# fast exponentiation:
# Find a power n (a^n in python without using **)
def fast_expo(a, n):
    """
    find a**n in log(n) time
    :param a: base (int)
    :param n: power (int)
    :return: a**n (int)
    """
    if n == 0:
        return 1

    half = fast_expo(a, n//2)
    ans = half * half
    if n % 2 == 0:
        return ans
    else:
        return a * ans

base = int(input("Enter base(a): "))
power = int(input("Enter power(n): "))
ans = fast_expo(base, power)
print("Fast {}^{}={}".format(base, power, ans))


