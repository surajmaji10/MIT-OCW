# fibbonacci series => Rabbit Breeding Model by Leonardo of Pisa (Fibbonacci) of Italy in 12th century
# don't go beyond 40 for n
def fibbonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

num = int(input('Enter a number n: '))
print("{}th fibbonacci is {}".format(num, fibbonacci(num)))

