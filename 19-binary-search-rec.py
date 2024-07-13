# this is a sample code from MIT OCW 18.00

def bin_search_rec(ls, low, high, key):
    if low > high:
        return -1
    
    mid = (low + high)//2

    if ls[mid] == key:
        return mid
    elif ls[mid] < key:
        return bin_search_rec(ls, mid+1, high, key)
    else:
        return bin_search_rec(ls, low, mid-1, high)
    
    