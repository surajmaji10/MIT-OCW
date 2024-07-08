
# iterating over key value pairs
mydict = {
    51: 515151,
    1:111,
    2:222,
    3:333,
    100: 100100100,
    4:444,
}
print(mydict)

# way 1
for k in mydict:
    print(k, mydict[k])

# way 2
for k in mydict.keys():
    print(k, mydict[k])

# way 3 (sorted fashion)
keys = list(mydict.keys())
keys.sort()
for k in keys:
    print(k, mydict[k])

# a simpler way
for key in sorted(list(mydict.keys())):
    print(key, mydict[key])

# simpler but same as above
for k, v in mydict.items():
    print(k, "=>" ,v)

