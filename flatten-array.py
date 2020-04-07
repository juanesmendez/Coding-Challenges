'''

Re-create Array.flat() — If you are not aware of what this function does, it accepts an input array that may contain nested arrays of unknown depth as elements and return a new array that is a flattened version of the input. In the scope of this problem, a flattened array refers to an array of all primitive values as elements within the array.
Example
Input: [1,[2,[3],4],[5]]
Output: [1,2,3,4,5]


'''

def flattenHelper(newArr, currentArray):
	for i in range(0, len(currentArray)):
		if(type(currentArray[i]) is list):
			flattenHelper(newArr, currentArray[i])
		elif currentArray[i] != None:
			newArr.append(currentArray[i])


def flatten(arr):
	if arr is None or len(arr) == 0:
		return []

	newArr = []
	flattenHelper(newArr, arr)
	return newArr





arr = [1, [[2], 3, 4, None], [[5]]]

print(type(arr))
print(flatten(arr)) # 1,2,3,4,5