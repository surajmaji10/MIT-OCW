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

def copy_list(src, dest):
    print("Adding {} to {}".format(src, dest))
    for item in src:
        dest.append(item)
    print("Done")

zs = [1, 2, 3]
ws = []
copy_list(zs, ws)
print(zs, ws)

bs = [1, 2, 3, 4, 5]
cs = []
#copy_list(bs, bs)
print(cs, bs)




