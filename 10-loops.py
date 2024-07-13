# python loops demo

for i in range(10, 0-1, -1):
    print("i = ", end="")
    print(i)


for i in range(0, 10):
    for j in range(0, 10):
        print((i,j), end= ", ")
        break

    print()

## GUESS GAME ##

import random

max_limit = 10
magic = random.randint(1, max_limit + 1)


guess = int(input("Make a guess (1-{}): ".format(max_limit)))
while guess != magic:
    print("Oops! {} is not correct. Try again.".format(guess))
    guess = int(input("Make a guess (1-100):"))

print("Yeah! You guessed it right. Its {}.".format(guess))


# while True:
#     guess = int(input("Make a guess (1-{}): ".format(max_limit)))
#     if guess != magic:
#         print("Oops! {} is not correct. Try again.".format(guess))
#     else:
#         break
# print("Yeah! You guessed it right. Its {}.".format(guess))


