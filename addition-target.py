'''

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

My solution complexity is O(N)
'''

def twoSum(arr, target):
	hashTable = {}
	populateTable(hashTable, arr)

	for i in range(0, len(arr)):
		desiredValue = target - arr[i]
		if validValueExists(desiredValue, hashTable, i):
			return [i, hashTable[desiredValue]]

	return [-1, -1]


def validValueExists(desiredValue, hashTable, currentIndex):
	# Make sure there exists a key with `desiredValue` and make sure we aren't re-using the same index
	return (hashTable[desiredValue] != None and hashTable[desiredValue] != currentIndex)


def populateTable(hashTable, arr):
	for i in range(0, len(arr)):
		hashTable[arr[i]] = i


print(twoSum([2, 1, 4, 3], 6)); # [0, 2]
print(twoSum([2, 7, 11, 15], 9)); # [0, 1]