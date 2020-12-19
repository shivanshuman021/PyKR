#undirected graph
import sys

def DFS(T,src):
	print(src,end=" ")

	for i in range(len(T)):
		if (T[src][i]):
			DFS(T,i)

def minval(G,dist,sptSet,src):
	# finds neighbourhood vertex at min distance
	minindex,minv = src,sys.maxsize

	for i in range(len(dist)):
		if dist[i]<minv and sptSet[i]==False:
			minindex,minv = i,dist[i]

	return minindex


def spanningTree(G,src):
	sptSet = [False for i in range(len(G))]
	dist = [sys.maxsize for i in range(len(G))]
	prev = [sys.maxsize for i in range(len(G))]
	dist[src] = 0
	prev[src] = 0

	u = 0

	for i in range(len(G)-1):
		u = minval(G,dist,sptSet,src)
		sptSet[u] = True

		for v in range(len(G)):
			if (sptSet[v]==False and G[u][v] and dist[v]>dist[u]+G[u][v]):
				dist[v] = dist[u] + G[u][v]
				prev[v] = u

	#print distance
	T = [[False for i in range(len(G))] for i in range(len(G))]

	for i in range(len(dist)):
		if i==src:
			continue

		T[prev[i]][i] = True

	DFS(T,src)

def printGraphMatrix(G):
	for i in G:
		for j in i:
			print(j,end=' ')
		print()


if __name__=="__main__":
	n,m = map(int,input().split())

	G = [[0 for i in range(n)] for i in range(n)]

	u,v,wt=0,0,0

	for i in range(m):
		u,v,wt = map(int,input().split())
		G[u][v] = G[v][u] = wt

	print("Enter source vertex : ")
	src = int(input())

	print("spanningTree is : ")
	spanningTree(G,src)


'''
9 14
0 1 4
0 7 8
1 2 8
1 7 11
2 3 7
2 5 4
2 8 2
3 4 9
3 5 14
4 5 10
5 6 2
6 7 1
6 8 6
7 8 7
'''




