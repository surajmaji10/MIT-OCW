# this is a sample code from MIT OCW 18.00


def lin_search1(xs, key):
    for x in xs:
        if x == key:
            return True
    return False

def lin_search2(xs, key):
    return key in xs


"""
assume xs is sorted for lin_search3()
"""
def lin_search3(xs, key):
    for x in xs:
        if x > key:
            return False
        elif x == key:
            return True
    return False

