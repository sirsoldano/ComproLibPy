# N頂点,N-1辺の連結グラフ＝木構造
# 単純パスは単一
# 1辺追加すると閉路が一つ出現

# 木の直径アルゴリズム (https://github.com/E869120/kyopro_educational_90/blob/main/editorial/003.jpg)
# 根付き木の最短距離を担う各辺重み＝部下数*(N-部下数)
def dfs(pos):
    node[pos] = 1
    for p in edge[pos]:
        if node[p]==0 : 
            dfs(p)
            node[pos] += node[p]
# 根付き木へのダブリングで最近共通祖先
class DubTree:
    def __init__(self,N):
        self.N, self.K = N, 1
        while (1<<self.K)<N : self.K += 1
        self.node,self.wei = [None]*self.N, [None]*self.N
        self.edge = [[] for n in range(self.N)]
        self.parent = [[None]*N for k in range(self.K)]
    def append_edge(self,a,b,w=1):
        self.edge[a].append((b,w)); self.edge[b].append((a,w))
    def dfs(self,s):
        stack, self.node[s],self.wei[s], self.parent[0][s] = [s], 0, 0, None
        while len(stack)>0:
            pos = stack.pop()
            for p,w in self.edge[pos]:
                if self.node[p] is None:
                    stack.append(p)
                    self.node[p], self.wei[p] = self.node[pos]+1, self.wei[pos]+w
                    self.parent[0][p] = pos
    def doubling(self):
        for k in range(self.K-1):
            for n in range(self.N):
                if self.parent[k][n] is None : self.parent[k+1][n] = None
                else : self.parent[k+1][n] = self.parent[k][self.parent[k][n]]
    def lca(self,a,b):
        if self.node[a]<self.node[b] : a,b=b,a
        for k in range(self.K-1,-1,-1):
            if self.node[a]-self.node[b]>=(1<<k) : a = self.parent[k][a]
        if a==b : return a
        for k in range(self.K-1,-1,-1):
            if self.parent[k][a]!=self.parent[k][b] : 
                a,b = self.parent[k][a],self.parent[k][b]
        return self.parent[0][a]
    def dist(self,a,b):
        lca = self.lca(a,b)
        return self.wei[a] + self.wei[b] - 2*self.wei[lca]

# オイラーツアー https://atcoder.jp/contests/abc294/submissions/50893914
class DubTree:
    def __init__(self,N):
        self.N, self.K = N, 1
        while (1<<self.K)<N : self.K += 1
        self.node,self.wei = [None]*self.N, [None]*self.N
        self.edge = [[] for n in range(self.N)]
        self.parent = [[None]*N for k in range(self.K)]
        self.euler = []
        self.eufl = [[0,0] for n in range(N)]
        self.fent = []
    def append_edge(self,a,b,w=1):
        self.edge[a].append((b,w)); self.edge[b].append((a,w))
    def dfs_dub(self,s):
        stack, self.node[s],self.wei[s] = [s], 0, 0
        self.parent[0][s] = None
        self._dfs(s)
        self._doubling()
        self.fent = [0]*(len(self.euler)+1)
    def _dfs(self,pos):
        self.euler.append(pos)
        self.eufl[pos][0] = len(self.euler)
        for p,w in self.edge[pos]:
            if self.node[p] is None:
                self.node[p], self.wei[p] = self.node[pos]+1, self.wei[pos]+w
                self.parent[0][p] = pos
                self._dfs(p)
                self.euler.append(pos)
        self.eufl[pos][1] = len(self.euler)
    def _doubling(self):
        for k in range(self.K-1):
            for n in range(self.N):
                if self.parent[k][n] is None : self.parent[k+1][n] = None
                else : self.parent[k+1][n] = self.parent[k][self.parent[k][n]]
    def lca(self,a,b):
        if self.node[a]<self.node[b] : a,b=b,a
        for k in range(self.K-1,-1,-1):
            if self.node[a]-self.node[b]>=(1<<k) : a = self.parent[k][a]
        if a==b : return a
        for k in range(self.K-1,-1,-1):
            if self.parent[k][a]!=self.parent[k][b] : 
                a,b = self.parent[k][a],self.parent[k][b]
        return self.parent[0][a]
    def dist(self,a,b):
        lca = self.lca(a,b)
        alen = self.wei[a] + self._sum(self.eufl[a][0]) - self.wei[lca] - self._sum(self.eufl[lca][0])
        blen = self.wei[b] + self._sum(self.eufl[b][0]) - self.wei[lca] - self._sum(self.eufl[lca][0])
        return alen + blen
    def add(self,a,i):
        n = self.eufl[a][0]
        while n<=len(self.fent)-1:
            self.fent[n]+=i
            n += n&-n
        n = self.eufl[a][1]+1
        while n<=len(self.fent)-1:
            self.fent[n]-=i
            n += n&-n
    def _sum(self,n):
        ans = 0
        while n>0:
            ans += self.fent[n]
            n -= n&-n
        return ans
