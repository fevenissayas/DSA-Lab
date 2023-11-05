arr = [2,3,4,0]

for i in range (len(arr)-1, 1, -1):
    arr[i] = arr [i-1]
arr[1] = 7
print (arr)
