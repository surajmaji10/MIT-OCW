# sample program from MIT-OCW 18.00
# program to check for the cube root of an integer
# ie. whether num is a perfect cube or not

num = int(input("Enter a integer: "))
n  = abs(num)

## way number 1
# for ans in range(0, n+1):
#     if ans ** 3 >= n:
#         break

# if ans ** 3 == n:
#     if  num < 0:
#         ans = ans * -1
#     print("The cube root of {} is {}".format(num, ans))
# else:
#     print("{} is not a perfect cube".format(num))

# way number 2
ans = 0
while ans*ans*ans < n:
    ans += 1

if ans*ans*ans == n:
    ans = -ans if n < 0 else ans
    print("The cube root of {} is {}".format(num, ans))
else:
    print("{} is not a perfect cube".format(num))


"""
Notion of decrementing function:

while ( 0 < (n - (ans)**3) )   eventually will halt as value becomes <= 0

"""

