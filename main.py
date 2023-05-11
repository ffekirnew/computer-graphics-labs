import numpy as np

numslist = [1, 2, 3, 4, 5]
arr = np.array(numslist)

#rank 1 array
print(arr)
type(arr)
arr.shape
print(arr[0], arr[1])
arr[1] = 9

#change an element of the array
print(arr[0], arr[1])