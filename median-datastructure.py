'''

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Design a data structure that supports the following two operations:
void addNum(int num) — Add a integer number from the data stream to the data structure.
double findMedian() — Return the median of all elements so far.

'''
class MyDataStructure:

	data = []

	def __init__():
		print("Inside constructor")
		#self.data = []


	def addNum(self, num):
		print("Do something...")
		if self.data is not None:
			self.data.append(num)


	def findMedian(self):
		print("Do something...")
		if len(self.data) % 2 == 0:
			return int((self.data[len(self.data) // 2] + self.data[(len(self.data) // 2) - 1]) / 2)
		else:
			return self.data[len(self.data) // 2]




myDataStruct = MyDataStructure
myDataStruct.addNum(myDataStruct, 5)
myDataStruct.addNum(myDataStruct, 8)
myDataStruct.addNum(myDataStruct, 12)
myDataStruct.addNum(myDataStruct, 4)
myDataStruct.addNum(myDataStruct, 10)
print(myDataStruct.data)
print(myDataStruct.findMedian(myDataStruct))
