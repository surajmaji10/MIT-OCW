
# find sum of digits of a number, say 1234

number_in_str = input("Enter a number: ")
print(number_in_str)

number = float(number_in_str)
assert number > 0

total = 0
for digit_str in number_in_str:
    if digit_str != '.':
        digit = int(digit_str)
        total += digit

print('The sum of all digits of', number_in_str, 'is:', total)

