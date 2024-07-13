import random


def integrate(f, a, b, num_trials=1000000):
    num_pins = 0
    for trials in range(num_trials):
        num_pins += f(random.uniform(a, b))
    avg = num_pins/num_trials
    return avg*(b-a)


def fun1(x):
    return 1.0


def fun2(x):
    return 1.0*x


def fun3(x):
    return 1.0*x*x


def fun4(x):
    return 1.0*x*x+2.0*x+5


print(integrate(fun1, 0, 100))
print(integrate(fun2, 0, 100))
print(integrate(fun3, 0, 9))
print(integrate(fun4, 0, 10))




