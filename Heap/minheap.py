import sys

class Minheap:
	# zero based indexing 
	def __init__(self):
		self.heap_size = 0
		self.H = []

	def parent(i):
		return (i-1)/2

	def left(self,i):
		return 2*i+1

	def right(self,i):
		return 2*i+2

	def insert(k):
		i = heap_size
		H[heap_size] = k
		heap_size+=1
		
		while i!=0 and H[parent(i)]>H[i]:
			H[i],H[self.parent(i)] = H[self.parent(i)],H[i]
			i = self.parent(i)


	def heapify(self,i):

		l = self.left(i)
		r = self.right(i)
		s = i #smallest
		
		if (l<self.heap_size and self.H[l]<self.H[s]):
			s = l
		
		if (r<self.heap_size and self.H[r]<self.H[s]):
			s = r
		
		if (s!=i):
			self.H[i],self.H[s] = self.H[s],self.H[i]
			self.heapify(s)

	def extractMin(self):
		if (self.heap_size<=0):
			return sys.maxsize

		root = self.H[0]
		self.heap_size-=1

		if (self.heap_size==0):
			return root

		self.H[0] = self.H[self.heap_size]
		H.heapify(0)

		return root

	def getMin():
		return H[0]

	def assign(self,a):
		self.H = a
		self.heap_size = len(a)
		self.heapify(0)

	def printHeap(self):
		for i in self.H:
			print(i,end=" ")


if __name__=="__main__":
	a = [10,3,61,9,8,7,6]

	H=Minheap()
	H.assign(a)
	#H.printHeap()
	while(H.heap_size>0):
		print(H.extractMin(),end=" ")

