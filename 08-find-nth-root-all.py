#######################################
##  find the nth root of a number x  ##
#######################################
# this is a sample code from MIT OCW 18.00
# find nth root any x (including -ve's)

x = float(input("Enter a number x to find root of: "))
n = int(input("Enter the power n for nth root: "))

def withinEpsilon(x, y, epsilon):
    """
    takes x and y to see if they differ by atmost epsilon
    x,y,z: float
    """
    #print("ans**n=", x, "x=", y, "true=", abs(x-y)<=epsilon)
    return abs(x-y)<=epsilon


def withinBounds(x, y):
    """
    checks if x is less than or equal to y
    x: float
    y: float
    """
    return x<=y

def findNthRootOf(x, n, epsilon=0.01):
    """
    find nth root of x within accuracy of epsilon
    x: float (any number)
    n: int (positive)
    epsilon: float (positive and small value like 0.0001 or so)
    """ 
    
    if x == 0:
        return 0
    # can't have imaginary root
    if x < 0 and n%2 == 0:
        return None

    assert type(x) == float and type(n) == int and type(epsilon) == float
    y = x
    x = abs(x)

    maxx = max(x, 1.0)
    low = 0
    high = maxx
    ans = (low + high)/2.0
    steps = 0
    while not withinEpsilon(ans**n, x, epsilon) and withinBounds(ans, maxx):
        if ans**n < x:
            low = ans
        else:
            high = ans

        ans = (low + high)/2.0
        steps += 1
    
    if withinEpsilon(ans**n, x, epsilon):
        if y < 0:
            ans = -ans
        print("Found in", steps, "steps.")
        return ans
    else:
        print("NOT Found in", steps, "steps.")
        return None

## call to see the results
ans = findNthRootOf(x, n, 0.0000000001)
if ans != None:
    print(f"{ans:f}", "is the", n, "th root of", x)
else:
    print("Could not find the {}th root of {}".format(n, x))


############## END ####################

