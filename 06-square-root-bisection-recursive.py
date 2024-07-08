
# bisection method (recursive)

def withinEpsilon(x, y, e):
    return abs(x-y) < e

def rec_bisection_sqroot(x, epsilon, low, high):

    maxx = max(x, 1.0)
    ans = (low + high)/2.0

    global steps
    steps += 1

    if withinEpsilon(ans*ans, x, epsilon) or ans > maxx:
        return ans 
    elif ans*ans < x:
        return rec_bisection_sqroot(x, epsilon, ans, high)
    else:
        return rec_bisection_sqroot(x, epsilon, low, ans)


# begin here
x = float(input("Enter a positive number: "))
maxx = max(x, 1.0)
epsilon = 0.001
low = 0
high = maxx #updated high as maxx not x

steps = 0
ans = rec_bisection_sqroot(x, epsilon, low, high)

if ans <= maxx:
    print(ans, "is the approx answer to", x, ". Taken", steps, "steps.")
else:
    print("Not Found", ". Taken", steps, "steps")





