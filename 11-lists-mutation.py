# show list mutaions and aliases

#xs = [2]
#ys = [xs, xs]
#print(xs, ys)
#
#xs[0] = 3
#print(xs, ys)
#
#xs = 4
#print(xs, ys)
#
#xs = ys[1]
#xs[0] = 5
#print(xs, ys)


# list aliases

# faulty copy list
def fcopy_list(src, dest):
    print("Copying {} to {}".format(src, dest))
    dest = []
    for item in src:
        dest.append(item)
    print("Copying Done", dest)

def copy_list(src, dest):
    print("Copying {} to {}".format(src, dest))
    while len(dest) > 0:
        dest.pop()
    for item in src:
        dest.append(item)
    print("Copying Done", dest)

def append_list(src, dest):
    print("Appending {} to {}".format(src, dest))
    for item in src:
        dest.append(item)
    print("Appending Done", dest)




zs = [1, 2, 3]
ws = [9]
fcopy_list(zs, ws)
print(zs, ws)

bs = [1, 2, 3, 4, 5]
cs = [6]
append_list(bs, cs)
print(bs, cs)

xs = [1, 2, 3, 4, 5]
ys = [6, 7]
copy_list(xs, ys)
print(xs, ys)






