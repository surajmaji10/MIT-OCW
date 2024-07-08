
# using exhaustive linear search

x = float(input("Enter a integer number: "))

epsilon = 0.01
increment = 0.001

ans = 0
steps = 0
while abs(ans*ans - x) >= epsilon and ans <= x:
    ans += increment
    steps += 1

if abs(ans*ans - x) < epsilon:
    print(ans, "is the approx sq. root of", x, ". Found in", steps, "steps.")
else:
    print("Not Found.", steps, "steps")

