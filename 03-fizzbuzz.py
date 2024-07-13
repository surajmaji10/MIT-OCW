# this is a sample code from MIT OCW 18.00

number = int(input("Enter a number: "))


# # way number 1
# for i in range(1, number+1):
# 	ans = str(i)
# 	if i % 3 == 0 or i % 5 == 0:
# 		ans = ""
# 		if i % 3 == 0:
# 			ans += "Fizz"
# 		if i % 5 == 0:
# 			ans += "Buzz"
# 	print(ans)


# way number 2
i = 1
while i <= number:
	ans = None
	if i % 5 == 0 and i % 3 == 0:
		ans = "FizzBuzz"
	elif i % 5 == 0:
		ans = "Buzz"
	elif i % 3 == 0:
		ans = "Fizz"
	else:
		ans = str(i)
	i += 1
	print(ans)

	
# end
	
