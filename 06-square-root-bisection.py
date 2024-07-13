# this is a sample code from MIT OCW 18.00
# using iterative binary search
# bisection method (faulty for values < 0): works with >=1 values only

x = float(input("Enter a positive real number (>=1): "))
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
    print("low:", low, "high:", high, "ans:", ans)
    steps += 1

if abs(ans*ans - x) < epsilon:
    print(ans, "is the approx answer to", x, ". Taken", steps, "steps.")
else:
    print("Not Found", ". Taken", steps, "steps")


