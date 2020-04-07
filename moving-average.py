'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
Example:
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''


class MovingAverage:

	data = []

	def __init__(self, windowSize):
		self.windowSize = windowSize


	def next(self, num):
		self.data.append(num)

		sum = 0
		if len(self.data) < self.windowSize:
			for i in range(0, len(self.data)):
				sum += self.data[i]

			return sum/len(self.data)
		else:
			start = len(self.data) - self.windowSize
			end = start + self.windowSize
			for i in range(start, end):
				sum += self.data[i]

			return sum/self.windowSize


movingAverage = MovingAverage(3)
#print(movingAverage.windowSize)

print(movingAverage.next(1))
print(movingAverage.next(10))
print(movingAverage.next(3))
print(movingAverage.next(5))
