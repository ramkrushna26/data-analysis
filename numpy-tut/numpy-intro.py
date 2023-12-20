import numpy as np

empty_arr = np.empty((3,4), dtype=int)
print("\nempty array: \n", empty_arr)

full_arr = np.full((3,4), 8, dtype=float)
print("\nfull array: \n", full_arr)

zero_arr = np.zeros((3,4), dtype=float)
print("\nfull array: \n", zero_arr)

one_arr = np.ones((3,4), dtype=float)
print("\nfull array: \n", one_arr)

arr = np.array([[10.5, 22.5, 3.8],  
				[23.45, 50, 78.7], 
				[41, np.nan, np.nan]]) 
print("\narr with non-numeric rows: \n", arr[~np.isnan(arr).any(axis=1)])

arr = np.array([[[1, 2, 3], [4, 5, 6]]]) 
print("\nbefore squeeze np array: \n", arr, arr.shape)
print("\nafter squeeze np array: \n", arr.squeeze(), arr.squeeze().shape)

print("\nTranspose arr: \n", arr.transpose())
print("\nTranspose arr: \n", np.array([[1,2,3]]).transpose())

num_1d = np.arange(5) 
num_2d = np.arange(10).reshape(2,5) 
print("\ncombining two arrays: \n1",num_1d, "\n2", num_2d)
for a, b in np.nditer([num_1d, num_2d]):
	print("%d:%d" % (a, b))

arr = np.array([1,2,3,4,5,1,2,1,10]) 
print("\nnumber of occurences: \n", np.bincount(arr))
print("\nelement with most occurences: \n", np.bincount(arr).argmax())

arr = np.array([[2, 8, 9, 4],  
                   [9, 4, 9, 4], 
                   [4, 5, 9, 7], 
                   [2, 9, 4, 3]]) 
print("\nsequence of occurences of (9.4): \n", arr, "\n===", repr(arr).count("9, 4"))



