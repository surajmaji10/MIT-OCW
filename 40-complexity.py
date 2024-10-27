import time

def foo(n):
    s = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                s += 1
    return s

t1 = time.time()
foo(100)
t2 = time.time()
print("The time taken is:", t2-t1)

def factorial(n):
    ans = 1
    while n > 1:
        ans = ans * n
        n = n - 1
    return ans

def factorial2(n):
    if n < 0:
        return -1
    if n < 2:
        return n
    return n * factorial2(n-1)

t1 = time.time()
print(factorial(100))
print(factorial2(100))
t2 = time.time()
print("The time taken is:", t2-t1)

def fibonacci(n):
    if n < 0:
        return -1
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibbonacci2(n):
    if n < 0:
        return -1
    if n < 2:
        return n
    x = 0
    y = 1
    for i in range(2, n+1):
        x, y = y, x+y
    return y

t1 = time.time()
print(fibonacci(40))
print(fibbonacci2(400))
t2 = time.time()
print("The time taken is:", t2-t1)
