# print a simple X-mas tree
height = int(input('Enter height of X-mas tree: '))

spaces = height-1
stars = 1
stump = height-1

while height > 0:

    for sp in range(spaces):
        print(" ", end="")
    for st in range(stars):
        print("#", end="")
    print()

    spaces -= 1
    stars += 2

    height -= 1

for st in range(stump):
    print(" ", end="")
print("#")