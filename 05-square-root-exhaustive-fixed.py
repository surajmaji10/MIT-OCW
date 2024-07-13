# this is a sample code from MIT OCW 18.00
# using exhaustive linear search
# this works for any x >= 0 (including b/w 0 and 1 unlike before)

x = float(input("Enter a integer number: "))
maxx = max(x, 1.0)

epsilon = 0.01
increment = 0.001

ans = 0
steps = 0
while abs(ans*ans - x) >= epsilon and ans <= maxx:
    ans += increment
    steps += 1

if abs(ans*ans - x) < epsilon:
    print(ans, "is the approx sq. root of", x, ". Found in", steps, "steps.")
else:
    print("Not Found.", steps, "steps,", "when ans=", ans)

