#######################################
##  find the nth root of a number x  ##
#######################################
# this is a sample code from MIT OCW 18.00
# find nth root any x >= 0

x = float(input("Enter a number x to find root of: "))
n = int(input("Enter the power n for nth root: "))

def withinEpsilon(x, y, epsilon):
    """
    takes x and y to see if they differ by atmost epsilon
    x,y,z: float
    """
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
    maxx = max(x, 1.0)
    low = 0
    high = maxx
    ans = (low + high)/2.0

    while not withinEpsilon(ans**n, x, epsilon) and withinBounds(ans, maxx):
        if ans**n < x:
            low = ans
        else:
            high = ans

        ans = (low + high)/2.0

    
    if withinEpsilon(ans**n, x, epsilon):
        return ans
    else:
        return None

## call to see the results
ans = findNthRootOf(x, n, 0.01)
if ans != None:
    print(ans, "is the", n, "th root of", x)
else:
    print("Could not find")


############## END ####################

