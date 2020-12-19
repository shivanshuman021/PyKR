from collections import deque

class BSTnode:
	def __init__(self,k):
		self.lc = None
		self.rc = None
		self.key = k


def find(BST,k):
	if (BST == None):
		return False

	if (BST.key == k):
		return True
	

	if (k<BST.key):
		return find(BST.lc,k)
	else:
		return find(BST.rc,k)


def insert(BST,k):
	if BST == None:
		return BSTnode(k)

	if (BST.key==k):
		return BST
	elif (k<BST.key):
		BST.lc = insert(BST.lc,k)
	else:
		BST.rc = insert(BST.rc,k)

	return BST

def inorder(BST):
	if (BST==None):
		return

	inorder(BST.lc)
	print(BST.key,end=" ")
	inorder(BST.rc)

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
	BST = None
	k = 0

	while 1:
		k = int(input())
		if (k==-1):
			break

		BST = insert(BST,k)

	
	BFT(BST)


