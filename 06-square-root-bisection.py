
# bisection method (faulty for values < 0): works with integers only

x = float(input("Enter a positive number: "))
epsilon = 0.001 # set as per need

low = 0
high = x

ans = (low + high)/2
steps = 0
while abs(ans*ans - x) >= epsilon and ans <= x:
    
    if ans*ans < x:
        low = ans
    else:
        high = ans

    ans = (low + high)/2
    steps += 1

if abs(ans*ans - x) < epsilon:
    print(ans, "is the approx answer to", x, ". Taken", steps, "steps.")
else:
    print("Not Found", ". Taken", steps, "steps")


