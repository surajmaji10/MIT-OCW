# this is a sample code from MIT OCW 18.00
# using iterative binary search
# bisection method: fixed for all real +ve x

x = float(input("Enter any positive real number (>= 0): "))
maxx = max(x, 1.0)

epsilon = 0.001 # set as per need

low = 0
high = maxx #updated high as maxx not x

ans = (low + high)/2
steps = 0
while abs(ans*ans - x) >= epsilon and ans <= maxx:
    
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


