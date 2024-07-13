# this is a sample code from MIT OCW 18.00

"""
assumption: array xs is always sorted
"""

def bin_search(arr, key):
    """
    input: int|float|str
    return True|False
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return True
    return False


def bin_search_idx(arr, key):
    """
    input: int|float|str
    return index (-1, 0, ....len(xs)-1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1
