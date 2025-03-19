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

# オイラーツアー
# https://atcoder.jp/contests/abc294/submissions/50893914
# https://atcoder.jp/contests/abc133/submissions/63951344
import sys; sys.setrecursionlimit(10**6); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
class DubTree:
    def __init__(self,N):
        self.N, self.K = N, 1
        while (1<<self.K)<N : self.K += 1
        self.node = [None]*self.N
        self.edge = [[] for n in range(self.N)]
        self.parent = [[None]*N for k in range(self.K)]
        self.euler = []
        self.postoeunum = [0]*N
        self.fent = []
        self.edgetoeunum = dict()
        self.fentc = []
    def _dfs(self,pos,bef):
        self.postoeunum[pos] = len(self.euler)
        self.euler.append(pos)
        for nex,d in self.edge[pos]:
            if nex!=bef:
                self.node[nex] = self.node[pos]+1
                self.edgetoeunum[(pos,nex)] = len(self.euler)
                self.parent[0][nex] = pos
                self._dfs(nex,pos)
                self.euler.append(pos)
                self.edgetoeunum[(nex,pos)] = len(self.euler)
    def _doubling(self):
        for k in range(self.K-1):
            for n in range(self.N):
                if self.parent[k][n] is None : self.parent[k+1][n] = None
                else : self.parent[k+1][n] = self.parent[k][self.parent[k][n]]
    def _lca(self,a,b):
        if self.node[a]<self.node[b] : a,b=b,a
        for k in range(self.K-1,-1,-1):
            if self.node[a]-self.node[b]>=(1<<k) : a = self.parent[k][a]
        if a==b : return a
        for k in range(self.K-1,-1,-1):
            if self.parent[k][a]!=self.parent[k][b] : 
                a,b = self.parent[k][a],self.parent[k][b]
        return self.parent[0][a]
    def _add(self,n,i):
        while n<=len(self.fent)-1:
            self.fent[n]+=i
            n += n&-n
    def _addc(self,n,i):
        while n<=len(self.fentc)-1:
            self.fentc[n]+=i
            n += n&-n
    def _sum(self,n):
        ret = 0
        while n>0:
            ret += self.fent[n]
            n -= n&-n
        return ret
    def _sumc(self,n):
        ret = 0
        while n>0:
            ret += self.fentc[n]
            n -= n&-n
        return ret
    def append_edge(self,a,b,d):
        self.edge[a].append((b,d)); self.edge[b].append((a,d))
    def make_euler(self,s):
        self.node[s] = 0
        self.parent[0][s] = None
        self._dfs(s,s)
        self._doubling()
        self.fent = [0]*(len(self.euler)+1)
        self.fentc = [0]*(len(self.euler)+1)
        for n in range(self.N):
            for p,d in self.edge[n]:
                if self.edgetoeunum[(n,p)]<self.edgetoeunum[(p,n)]:
                    self._add(self.edgetoeunum[(n,p)],d)
                    self._add(self.edgetoeunum[(p,n)],-d)
    def dist(self,a,b):
        lca = self._lca(a,b)
        alen = self._sum(self.postoeunum[a])-self._sum(self.postoeunum[lca])
        blen = self._sum(self.postoeunum[b])-self._sum(self.postoeunum[lca])
        return alen + blen
    def cnt(self,a,b):
        lca = self._lca(a,b)
        alen = self._sumc(self.postoeunum[a])-self._sumc(self.postoeunum[lca])
        blen = self._sumc(self.postoeunum[b])-self._sumc(self.postoeunum[lca])
        return alen + blen
    def add_d(self,a,b,d):
        if self.edgetoeunum[(a,b)]<self.edgetoeunum[(b,a)]:
            self._add(self.edgetoeunum[(a,b)],d)
            self._add(self.edgetoeunum[(b,a)],-d)
            self._addc(self.edgetoeunum[(a,b)],-d//abs(d))
            self._addc(self.edgetoeunum[(b,a)],d//abs(d))
        else:
            self._add(self.edgetoeunum[(a,b)],-d)
            self._add(self.edgetoeunum[(b,a)],d)
            self._addc(self.edgetoeunum[(a,b)],d//abs(d))
            self._addc(self.edgetoeunum[(b,a)],-d//abs(d))


# Trie木
tree,ans = {},0
for n in range(N):
  temp = tree
  for c in s[n]:
    if c in temp:
      ans+=temp[c][0]
      temp[c][0]+=1
    else:
      temp[c] = [1,{}]
    temp = temp[c][1]
print(ans)

# 重心分解
N = int(input())
edge,parent,nodenum = [set() for n in range(N)],[None]*N,[None]*N
for m in range(N-1):
    a,b = map(int,input().split())
    edge[a-1].add(b-1)
    edge[b-1].add(a-1)
def dfs(pos):
    nodenum[pos] = 1
    for p in edge[pos]:
        if nodenum[p] is None : 
            nodenum[pos] += dfs(p)
    return nodenum[pos]
def getroot(r):
    while True:
        for p in edge[r]:
            if nodenum[p]*2 > nodenum[r]:
                nodenum[r], nodenum[p] = nodenum[r]-nodenum[p], nodenum[r]
                r = p
                break
        else:
            break
    return r
