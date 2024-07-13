
# this is a sample program from MIT-OCW 6.00
# heron of alexandria (ancient greece)

number = float(input("Enter a number: "))
assert number >= 0

# start with any random guess
guess = number/2
# assuming a tolerance of within 0.0001
# continually average g and x/g

print("Guess:", guess, "Guess**2:", guess**2, "Number:", number, "New Guess:", (guess + number/guess)/2)
while abs(guess * guess - number) > 0.0001:
    guess = (guess + number/guess)/2
    print("Guess:", guess, "Guess**2:", guess**2, "Number:", number, "New Guess:", (guess + number/guess)/2)

print("The square root of the number (using heron algo)", number, "is", guess)
print("The square root of the number (using ** operator)", number, "is", number**0.5)



