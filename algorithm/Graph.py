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
# PyPyだとたまにTLEするのでその場合はPythonで提出
def dfs(pos):
    node[pos] = 1
    for p in edge[pos]:
        if node[p]==0 : dfs(p)
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
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ap, https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bl
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

# 経路復元 探索時に一つ前のnode番号をnodeに記録しておく
def getpath(t):
    path = []
    while t != 0:
        path.append(t)
        t = node[t]
    path.reverse()
    return path

# 強連結性成分分解 https://atcoder.jp/contests/typical90/submissions/35212815
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/021.jpg
class SCC:
    def __init__(self,N):
        self._n = N
        self.teds = [[] for n in range(N)]
        self.reds = [[] for n in range(N)]
        self.nnums = []
        self.used = [False]*N
        self.inc = 0
    def addedge(self,a,b):
        self.teds[a].append(b)
        self.reds[b].append(a)
    def tdfs(self,pos):
        self.used[pos]=True
        for p in self.teds[pos] :
            if self.used[p]==False:
                self.tdfs(p)
        self.nnums.append(pos)
    def rdfs(self,pos):
        self.used[pos]=False
        self.inc += 1
        for p in self.reds[pos] :
            if self.used[p]==True:
                self.rdfs(p)

# 最大フロー問題(Dinic法)
# 解説 https://tjkendev.github.io/procon-library/python/max_flow/dinic.html
from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.e = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.e[fr].append(forward)
        self.e[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.e[v1].append(edge1)
        self.e[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        e = self.e
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in e[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10000000000000000000
        e = self.e
        while self.bfs(s, t):
            *self.it, = map(iter, self.e)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow
# 燃やす埋める問題(https://atcoder.jp/contests/typical90/tasks/typical90_an)
# 解説 https://zenn.dev/kiwamachan/articles/37a2c646f82c7d

# 単一始点最短経路問題、全点対間最短経路問題(Warshall-Floyd:N^3)
# 二部マッチング(Hopcroft-Karp:M√N)
