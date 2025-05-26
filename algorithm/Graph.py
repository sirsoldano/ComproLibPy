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
N,M = map(int,input().split())
edge,node=[[] for n in range(N)],[1<<60]*N
for m in range(M):
    a,b,c = map(int,input().split())
    edge[a-1].append((b-1,c))
    edge[b-1].append((a-1,c))
import heapq as hq
def dijkstra(s):
    q = []
    hq.heappush(q,(0,s))
    while len(q)>0 :
        dist,pos = hq.heappop(q)
        if node[pos] < 1<<60 : continue
        node[pos] = dist
        for p,d in edge[pos]:
            if node[p] > dist+d:
                hq.heappush(q,(dist+d,p))
dijkstra(0)
print(node[N-1]) if node[N-1]<1<<60 else print(-1)
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
for n in range(N-1):
#  update = False
  for a in range(N):
    for b,c in edge[a]:
      if d[a]<1<<60 and d[b] > d[a] + c:
        d[b] = d[a] + c
#        update = True
#  if update==False : break
# 負閉路を見つける場合は再更新。1つでも見つければ良いのならば1回。N-1などある頂点が影響を受ける負閉路かを判断するにはN回更新
# https://atcoder.jp/contests/abc061/tasks/abc061_d

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
# ループ内マーキング方式も可 https://atcoder.jp/contests/abc296/submissions/40271239
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

# functional graph
N = int(input())
a = [*map(lambda x:int(x)-1,input().split())]
heiro,visited = [],[0]*N
for n in range(N):
  if visited[n]:continue
  root = []
  while visited[n]==0:
    root.append(n)
    visited[n]=1
    n = a[n]
  if n not in root : continue
  heiro.append(root[root.index(n):])

# 最大フロー問題(Dinic法)
# 解説 https://tjkendev.github.io/procon-library/python/max_flow/dinic.html
from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.flolas = [[0]*N for n in range(N)]
        self.e = [[] for n in range(N)]
    def add_edge(self, fr, to, cap):
        self.flolas[fr][to] = cap
        self.flolas[to][fr] = 0
        self.e[fr].append(to)
        self.e[to].append(fr)
    def bfs(self, s, t):
        self.level = [None]*self.N
        deq = deque([s])
        self.level[s] = 0
        while deq:
            pos = deq.popleft()
            for p in self.e[pos]:
                cap = self.flolas[pos][p]
                if cap>0 and self.level[p] is None:
                    self.level[p] = self.level[pos] + 1
                    deq.append(p)
        return self.level[t] is not None
    def dfs(self, pos, t, f):
        if pos == t : return f
        for p in self.it[pos]:
            cap = self.flolas[pos][p]
            if cap>0 and self.level[pos] < self.level[p]:
                d = self.dfs(p, t, min(f, cap))
                if d:
                    self.flolas[pos][p] -= d
                    self.flolas[p][pos] += d
                    return d
        return 0
    def flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            *self.it, = map(iter, self.e)
            while True:
                f = self.dfs(s, t, 1<<60)
                if f==0 : break
                flow += f
        return flow
    def cut(self,s):
        deq = deque([s])
        sside = {s}
        while deq:
            pos = deq.popleft()
            flag = True
            for p in self.e[pos]:
                if self.flolas[pos][p]>0 and p not in sside:
                    flag = False
                    sside.add(p)
                    deq.append(p)
        return sside
# Dinic (dict ver)
from collections import deque, Counter
class Dinic:
    def __init__(self, N):
        self.N = N
        self.graph = [[] for _ in range(N)]
        self.capacity = Counter()

    def add_edge(self, fr, to, cap):
        self.graph[fr].append(to)
        self.graph[to].append(fr)
        self.capacity[(fr, to)] += cap
        self.capacity[(to, fr)] += 0

    def bfs(self, s, t):
        self.level = [None]*self.N
        queue = deque([s])
        self.level[s] = 0
        while queue:
            v = queue.popleft()
            for to in self.graph[v]:
                if self.capacity[(v, to)] > 0 and self.level[to] is None:
                    self.level[to] = self.level[v] + 1
                    queue.append(to)
        return self.level[t] is not None

    def dfs(self, v, t, upTo):
        if v == t:
            return upTo
        for i in range(self.iter[v], len(self.graph[v])):
            to = self.graph[v][i]
            if self.capacity[(v, to)] > 0 and self.level[v] < self.level[to]:
                d = self.dfs(to, t, min(upTo, self.capacity[(v, to)]))
                if d > 0:
                    self.capacity[(v, to)] -= d
                    self.capacity[(to, v)] += d
                    return d
            self.iter[v] += 1
        return 0

    def flow(self, s, t):
        total = 0
        INF = 1 << 60
        while self.bfs(s, t):
            self.iter = [0] * self.N
            while True:
                f = self.dfs(s, t, INF)
                if f == 0:
                    break
                total += f
        return total

# minimum cost flow slope https://atcoder.jp/contests/abc407/tasks/abc407_g
import heapq
class mcf_graph():
    n=1
    pos=[]
    g=[[]]
    def __init__(self,N):
        self.n=N
        self.pos=[]
        self.g=[[] for i in range(N)]
    def add_edge(self,From,To,cap,cost):
        assert 0<=From and From<self.n
        assert 0<=To and To<self.n
        m=len(self.pos)
        self.pos.append((From,len(self.g[From])))
        self.g[From].append({"to":To,"rev":len(self.g[To]),"cap":cap,"cost":cost})
        self.g[To].append({"to":From,"rev":len(self.g[From])-1,"cap":0,"cost":-cost})
    def get_edge(self,i):
        m=len(self.pos)
        assert 0<=i and i<m
        _e=self.g[self.pos[i][0]][self.pos[i][1]]
        _re=self.g[_e["to"]][_e["rev"]]
        return {"from":self.pos[i][0],"to":_e["to"],"cap":_e["cap"]+_re["cap"],
        "flow":_re["cap"],"cost":_e["cost"]}
    def edges(self):
        m=len(self.pos)
        result=[{} for i in range(m)]
        for i in range(m):
            tmp=self.get_edge(i)
            result[i]["from"]=tmp["from"]
            result[i]["to"]=tmp["to"]
            result[i]["cap"]=tmp["cap"]
            result[i]["flow"]=tmp["flow"]
            result[i]["cost"]=tmp["cost"]
        return result
    def flow(self,s,t,flow_limit=-1-(-1<<63)):
        return self.slope(s,t,flow_limit)[-1]
    def slope(self,s,t,flow_limit=-1-(-1<<63)):
        assert 0<=s and s<self.n
        assert 0<=t and t<self.n
        assert s!=t
        dual=[0 for i in range(self.n)]
        dist=[0 for i in range(self.n)]
        pv=[0 for i in range(self.n)]
        pe=[0 for i in range(self.n)]
        vis=[False for i in range(self.n)]
        def dual_ref():
            for i in range(self.n):
                dist[i]=-1-(-1<<63)
                pv[i]=-1
                pe[i]=-1
                vis[i]=False
            que=[]
            heapq.heappush(que,(0,s))
            dist[s]=0
            while(que):
                v=heapq.heappop(que)[1]
                if vis[v]:continue
                vis[v]=True
                if v==t:break
                for i in range(len(self.g[v])):
                    e=self.g[v][i]
                    if vis[e["to"]] or (not(e["cap"])):continue
                    cost=e["cost"]-dual[e["to"]]+dual[v]
                    if dist[e["to"]]-dist[v]>cost:
                        dist[e["to"]]=dist[v]+cost
                        pv[e["to"]]=v
                        pe[e["to"]]=i
                        heapq.heappush(que,(dist[e["to"]],e["to"]))
            if not(vis[t]):
                return False
            for v in range(self.n):
                if not(vis[v]):continue
                dual[v]-=dist[t]-dist[v]
            return True
        flow=0
        cost=0
        prev_cost=-1
        result=[(flow,cost)]
        while(flow<flow_limit):
            if not(dual_ref()):
                break
            c=flow_limit-flow
            v=t
            while(v!=s):
                c=min(c,self.g[pv[v]][pe[v]]["cap"])
                v=pv[v]
            v=t
            while(v!=s):
                self.g[pv[v]][pe[v]]["cap"]-=c
                self.g[v][self.g[pv[v]][pe[v]]["rev"]]["cap"]+=c
                v=pv[v]
            d=-dual[s]
            flow+=c
            cost+=c*d
            if(prev_cost==d):
                result.pop()
            result.append((flow,cost))
            prev_cost=cost
        return result

# 燃やす埋める問題(https://atcoder.jp/contests/typical90/tasks/typical90_an)
# 解説 https://zenn.dev/kiwamachan/articles/37a2c646f82c7d

# 最小費用フロー https://atcoder.jp/contests/abc247/submissions/53489839
# https://tjkendev.github.io/procon-library/python/min_cost_flow/primal-dual.html
from heapq import heappush, heappop
class MinCostFlow:
    def __init__(self, N):
        self.N = N
        self.edge = [[] for i in range(N)] 
        # [to, cap, cost, rev]
    def addEdge(self, f, t, cap, cost):
        forward = [t, cap, cost, None]
        backward = forward[3] = [f, 0, -cost, forward]
        self.edge[f].append(forward)
        self.edge[t].append(backward)
    def minCostFlow(self, s, t, f):
        N = self.N; G = self.edge
        INF = 1<<60
        res = 0
        H = [0]*N
        prv_v = [0]*N
        prv_e = [None]*N

        d0 = [INF]*N
        dist = [INF]*N

        while f:
            dist[:] = d0
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                r0 = dist[v] + H[v]
                for e in G[v]:
                    w, cap, cost, _ = e
                    if cap > 0 and r0 + cost - H[w] < dist[w]:
                        dist[w] = r = r0 + cost - H[w]
                        prv_v[w] = v; prv_e[w] = e
                        heappush(que, (r, w))
            if dist[t] == INF:
                return None

            for i in range(N):
                H[i] += dist[i]

            d = f; v = t
            while v != s:
                d = min(d, prv_e[v][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = prv_e[v]
                e[1] -= d
                e[3][1] += d
                v = prv_v[v]
        return res
# 解説 https://ikatakos.com/pot/programming_algorithm/graph_theory/bipartite_matching

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

# Bridge(橋)判定のアルゴリズム https://nupioca.hatenadiary.jp/entry/2013/11/03/200006 , https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2017/1014_abc075
# 例題：https://atcoder.jp/contests/abc375/tasks/abc375_g
import sys; sys.setrecursionlimit(10**6); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def dfs(v, p, a):
    if pre[v] != -1:
        low[a] = min(low[a], low[v])
        return low[a]
    pre[v] = p
    low[v] = p
    for u in edge[v]:
        if u != a : low[v] = min(low[v], dfs(u, p + 1, v))
    if pre[v] == low[v] and a is not None : ans[e[(v,a)]]="Yes"
    return low[v]
pre,low = [-1]*N,[-1]*N
dfs(0,0,None)

# 単一始点最短経路問題、全点対間最短経路問題(Warshall-Floyd:N^3)
# 二部マッチング(Hopcroft-Karp:M√N)
