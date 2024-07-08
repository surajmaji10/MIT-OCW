## check list|tuple|string arr is sorted or not
def check_sorted(arr):
    """
    check if the passed list `arr` is sorted or not
    :param arr: a list|tuple of ints|floats|string or a string
    :return: True if arr is sorted else False
    """
    if len(arr) <= 1:
        return True
    return arr[0] <= arr[1] and check_sorted(arr[1:])

## all these lists below work
# ls = [1, 2, 3, 4, 5, 6, 7, 8]
# ls = (10, 12, 13, 16, 18)
# ls = "abcdefghjkli"
ls = ["my", "name", "operates", "power"]
print("object {} is sorted? {}".format(ls, check_sorted(ls)))

