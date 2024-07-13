# this is a sample code from MIT OCW 18.00
# using exhaustive linear search
# this currently doesn't have capability to handle x < 1.0

x = float(input("Enter a real number (>=1): "))

epsilon = 0.0001
increment = 0.001

ans = 0
steps = 0
# why have this ans <= x ? check be there?
# when increment > epsilon we may have difference `ans*ans - x` always more than `epsilon``
while abs(ans*ans - x) >= epsilon and ans <= x:
    ans += increment
    steps += 1

if abs(ans*ans - x) < epsilon:
    print(ans, "is the approx sq. root of", x, ". Found in", steps, "steps.")
else:
    print("Not Found.", steps, "steps,", "when ans=", ans)

print("By using ** operator:", x**0.5)

