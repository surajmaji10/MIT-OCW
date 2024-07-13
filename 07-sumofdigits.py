# sample program from MIT-OCW 18.00

n = int(input("Enter an integer: "))
m = n
n = abs(n)

summ = 0
while n > 0:
    r = n % 10
    summ += r
    n = n // 10

print('The sum of digits of n =', m, "is:", summ)
