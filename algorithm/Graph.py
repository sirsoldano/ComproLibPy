# https://hcpc-hokudai.github.io/archive/graph_shortest_path_mst_001.pdf
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
from collections import deque
q = deque()
q.append(0)
node[0]=0
while q:
    pos = q.popleft()
    for p in edge[pos]:
        if node[p]==-1:
            q.append(p)
            node[p]=node[pos]+1
# Dijkstra法
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ap, https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bl
import heapq
edge = [(nn,dist) for n in range(N)]
def dijkstra(s):
    q = []
    heapq.heappush(q,(0,s))
    node[s] = 0
    while len(q)>0 :
        pos = heapq.heappop(q)
        for p,dist in edge[pos[1]]:
            if node[p] is None or node[p]>pos[0]+dist:
                node[p] = pos[0]+dist
                heapq.heappush(q,(node[p],p))
# Warshall-Floyd(tc:N^3)
abc,d=[],[[1<<60]*N for n in range(N)]
for m in range(M):
    a,b,c = map(int,input().split())
    d[a-1][b-1]=c
    d[b-1][a-1]=c
    abc.append((a-1,b-1,c))
for a in range(N):
    for b in range(N):
        for c in range(N):
            d[b][c] = min(d[b][c],d[b][a]+d[a][c])
# Bellman-Ford
d = [0]+[1<<60]*(N-1)
for n in range(N):
  update = []
  for a in range(N):
    for b,c in edge[a]:
      if d[a]<1<<60 and d[b] > d[a] + c:
        d[b] = d[a] + c
        update.append(b)
  if len(update)==0 : break
# トポロジカルソート (有向グラフの閉路検出にも)
q = deque()
for n in range(N):
    if node[n]==0:
        q.append(n)
ans = []
while q:
    v = q.popleft()
    ans.append(v)
    for s in edge[v]:
        node[s] -= 1
        if node[s]==0:
            q.append(s)
# 深さありトポロジカルソート
stack=[]
for n in range(N):
    if node[n]==0:
        stack.append(n)
temp = [-1]*N
ans = []
def dfs(dep):
    if dep==N:
        ans.append(tuple(temp))
        return True
    if len(stack)==0 : return False
    for n in range(len(stack)-1,-1,-1):
        if len(ans)==K : break
        s = stack.pop(n)
        for p in edge[s]:
            node[p]-=1
            if node[p]==0 : stack.append(p)
        temp[dep]=s+1
        if not dfs(dep+1) : return False
        for p in edge[s]:
            if node[p]==0 : stack.pop()
            node[p]+=1
        stack.insert(n,s)
    return True
dfs(0)
# 閉路検出
def dfsloop(pos,bef):
    node[pos] = 1
    for p in edge[pos]:
        if node[p]==0 : 
            if dfsloop(p,pos):
                loop.append(p)
                if pos==loop[0]:
                    loop.append(pos)
        else:
            loop.append(p)
            if p==pos and len(loop)==1 : loop.append(p)
            return True
        if len(loop)>0 : 
            return loop[0]!=loop[-1]
    return False
for n in range(N):
    loop = []
    if node[n]==0 : dfsloop(n,-1)
    if len(loop)<=1 or loop[0]!=loop[-1] : continue
# DSmaze
H,W = map(int,input().split())
edge = [list() for n in range(H*W)]
node = sum([list(map(lambda x:False if x=="#" else -1,input().rstrip())) for h in range(H)],[])
for h in range(H):
    for w in range(W):
        if w<W-1 and node[h*W+w] and node[h*W+w+1]:
            edge[h*W+w].append(h*W+w+1)
            edge[h*W+w+1].append(h*W+w)
        if h<H-1 and node[h*W+w] and node[h*W+w+W]:
            edge[h*W+w].append(h*W+w+W)
            edge[h*W+w+W].append(h*W+w)
edge = [[list() for w in range(W)] for h in range(H)]
node = [list(map(lambda x:False if x=="#" else -1,input().rstrip())) for h in range(H)]
for h in range(H):
    for w in range(W):
        if w<W-1 and node[h][w] and node[h][w+1]:
            edge[h][w].append((h,w+1,1))
            edge[h][w+1].append((h,w,3))
        if h<H-1 and node[h][w] and node[h+1][w]:
            edge[h][w].append((h+1,w,0))
            edge[h+1][w].append((h,w,2))
H,W = map(int,input().split())
mp = [list(map(lambda x:int(x=="."),input().rstrip())) for h in range(H)]
node = [[None]*W for h in range(H)]
q,node[0][0] = deque(),0
q.append((0,0))
while q:
    h,w = q.popleft()
    for dh,dw in ((1,0),(0,1),(-1,0),(0,-1)):
        if 0<=h+dh<H and 0<=w+dw<W and mp[h+dh][w+dw] and node[h+dh][w+dw] is None:
            q.append((h+dh,w+dw))
            node[h+dh][w+dw] = node[h][w]+1

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

# 巡回セールスマン問題(bitDP) N=20まで https://qiita.com/Ll_e_ki/items/fa475f5bb224ada9be97
# ABC301E https://atcoder.jp/contests/abc301/submissions/41428508
# ABC274E https://atcoder.jp/contests/abc274/submissions/47607269
dp=[[1<<60]*N for b in range(1<<N)]
for n in range(1,N) : dp[1<<n][n] = d[0][n]
for b in range(2,(1<<N)-1):
    for fr in range(1,N):
        for to in range(N):
            if (1<<fr)&b==0 : continue
            if (1<<to)&b==0 and dp[b][fr]+d[fr][to] < dp[b|(1<<to)][to]:
                dp[b|(1<<to)][to] = dp[b][fr]+d[fr][to]
print(dp[(1<<N)-1][0])
# 負の辺あり & notConnectedの可能性あり　ABC338F https://atcoder.jp/contests/abc338/tasks/abc338_f
dp=[[1<<60]*N for b in range(1<<N)]
for n in range(N) : dp[1<<n][n] = 0
for b in range(1,(1<<N)-1):
    for fr in range(N):
        if (1<<fr)&b==0 or dp[b][fr]==1<<60 : continue
        for to in range(N):
            if (1<<to)&b==0 and d[fr][to]<1<<60 and dp[b][fr]+d[fr][to] < dp[b|(1<<to)][to]:
                dp[b|(1<<to)][to] = dp[b][fr]+d[fr][to]
print(min(dp[(1<<N)-1])) if min(dp[(1<<N)-1])<1<<60 else print("No")

# 単一始点最短経路問題、全点対間最短経路問題(Warshall-Floyd:N^3)
# 二部マッチング(Hopcroft-Karp:M√N)
