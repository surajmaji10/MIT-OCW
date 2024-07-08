# keys must be immutable (can't be lists or can't contain lists)
ls = [2, 3, 5, 7]
tup = (2.0, True, 2, 'b', "GOOD", ((2, 3), 2))
# tup = (2.0, True, 2, 'b', "GOOD", ((2, 3), 2)) # can't  have a list anywhere
ys = (2, 3, 5, 7)
mydict = {
    tup: "A tuple containing list",
    2: "A two",
    3.0: "A three point 0",
    False: "A false value",
    ys: ls
}
print(mydict)

