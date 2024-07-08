
# this is a sample program from MIT-OCW 6.00

number = float(input("Enter a number: "))

guess = number/2

while abs(guess * guess - number) > 0.0001:
    guess = (guess + number/guess)/2

print("The square root of the number", number, "is", guess)

# end

