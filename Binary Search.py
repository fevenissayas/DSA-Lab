arr = [2,3,4,5,6,8]
low = 0
high = len (arr) - 1

def BinarySearch (target, low, high, arr):
    
    if high >= low:  
        mid = (high + low)//2  
        if arr [mid] == target:
            return mid
        if arr [mid] > target:
            return BinarySearch (target, low, mid - 1, arr)
        if arr [mid] < target:
            return BinarySearch (target, low + 1, high, arr)

    return -1

result = BinarySearch (7, low, high, arr)
print (result)