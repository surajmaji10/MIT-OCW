
# find sum of digits of a number, say 1234

number = int(input("Enter a number: "))
assert number > 0
number_in_str = str(number)
total = 0
for digit_str in number_in_str:
    digit = int(digit_str)
    total += digit
print('The sum of all digits of', number, 'is:', total)

