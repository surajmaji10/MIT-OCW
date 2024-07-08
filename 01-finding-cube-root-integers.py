# program to check for the cube root of an integer

num = int(input("Enter a integer: "))
n  = abs(num)

for ans in range(0, n+1):
    if ans ** 3 >= n:
        break

if ans ** 3 == n:
    if  num < 0:
        ans = ans * -1
    print("The cube root of {} is {}".format(num, ans))
else:
    print("{} is not a perfect cube".format(num))

