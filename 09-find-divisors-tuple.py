########################
## Prohram to find the set of all divisors of a number n
########################

num = int(input("Enter a number: "))
divisors = ()
for div in range(1, num+1):
    if num % div == 0:
        divisors += (div,)
        print(divisors)

print("The divisors of number", num, "are", divisors)


