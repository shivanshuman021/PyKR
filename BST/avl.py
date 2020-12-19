# avl tree implementation in python
from collections import deque

class node:
	def __init__(self,k):
		self.lc = None
		self.rc = None
		self.key = k
		self.h = 1


def find(T,k):
	if (T == None):
		return False

	if (T.key == k):
		return True

	if (k<T.key):
		return find(T.lc,k)
	else:
		return find(T.rc,k)

def height(T):
	if (T==None):
		return 0
	return T.h

def left(T):
	root = T.rc
	D = root.lc

	root.lc = T
	root.lc.rc = D

	T.h = 1+max(height(T.lc),height(T.rc))
	root.h = 1+max(height(root.lc),height(root.rc))
	return root

def right(T):
	root = T.lc
	D = root.rc

	root.rc = T
	root.rc.lc = D

	T.h = 1+max(height(T.lc),height(T.rc))
	root.h = 1+max(height(root.lc),height(root.rc))
	return root

def loadf(T):
	if (T==None):
		return 0
	return height(T.lc) - height(T.rc)

def insert(T,k):
	if T == None:
		return node(k)

	if (k<T.key):
		T.lc = insert(T.lc,k)
	elif (k>T.key):
		T.rc = insert(T.rc,k)
	else:
		return T

	T.h = 1+max(height(T.lc),height(T.rc))	

	f = loadf(T)

	if f<-1:
		if k<T.rc.key:
			print("right at "+T.rc.key+'\n')
			T.rc = right(T.rc)
		T = left(T)

	elif f>1:
		if k>T.lc.key:
			print("left at "+T.lc.key+'\n')
			T.lc = left(T.lc)
		T = right(T)

	return T

def inorder(T):
	if (T==None):
		return

	inorder(T.lc)
	print(T.key,end=" ")
	inorder(T.rc)

def BFT(T):
	if (T==None):
		return

	q = deque()
	q.append(T)

	while len(q)>0:
		k = q[0]
		print(k.key,end=" ")
		
		if (q[0].lc):
			q.append(q[0].lc)
		if(q[0].rc):
			q.append(q[0].rc)
		q.popleft()


if __name__=="__main__":
	T = None
	k = 0

	while 1:
		k = int(input())
		if (k==-1):
			break

		T = insert(T,k)
		BFT(T)
		print()

