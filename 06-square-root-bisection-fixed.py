
# bisection method

x = float(input("Enter a positive number: "))
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


