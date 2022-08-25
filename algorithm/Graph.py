import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
edge,node=[[] for n in range(N)],[-1]*N
for m in range(M):
	a,b = map(int,input().split())
	edge[a-1].append(b-1)
	edge[b-1].append(a-1)

# tc : N+M
def dfs(pos):
	node[pos] = 1
	for p in edge[pos]:
		dfs(p) if node[p]==0 else None
def dfs(s):
	stack=[s]
	node[s]=1
	while len(stack)>0:
		pos = stack.pop()
		for p in edge[pos]:
			if node[p]==-1:
				stack.append(p)
				node[p]=1
# tc : N+M
import queue
def bfs(s):
	q = queue.Queue()
	q.put(s)
	node[s]=0
	while not q.empty():
		pos = q.get()
		for p in edge[pos]:
			if node[p]==-1:
				q.put(p)
				node[p]=node[pos]+1
# Dijkstra法
import heapq
edge = [{nn:dist} for n in range(N)]
def dijkstra(s):
	q = []
	heapq.heappush(q,(0,s))
	while len(q)>0 :
		pos = heapq.heappop(q)
		for p,dist in edge[pos[1]].items():
			if node[p]==-1 or node[p]>pos[0]+dist:
				node[p] = pos[0]+dist
				heapq.heappush(q,(node[p],p))
# DSmaze
H,W = map(int,input().split())
edge = [list() for n in range(H*W)]
node = sum([list(map(lambda x:0 if x=="#" else -1,input().rstrip())) for h in range(H)],[])
direc = (1,W) # 左上から処理するので右と下だけ
for h in range(1,H-1):
	for w in range(1,W-1):
		for d in direc:
			if node[h*W+w] and node[h*W+w+d]:
				edge[h*W+w].append(h*W+w+d)
				edge[h*W+w+d].append(h*W+w)
# 単一始点最短経路問題、全点対間最短経路問題(Warshall-Floyd:N^3)
# 最大フロー問題(Ford-Fulkerson、Dinic)、二部マッチング(Hopcroft-Karp:M√N)
