# this is a sample code from MIT OCW

number = int(input("Enter a number: "))

for i in range(1, number+1):
	ans = str(i)
	if i % 3 == 0 or i % 5 == 0:
		ans = ""
		if i % 3 == 0:
			ans += "Fizz"
		if i % 5 == 0:
			ans += "Buzz"
	print(ans)
	
# end
	
