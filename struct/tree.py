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
        self.N = N
        self.K = 1
        while (1<<self.K)<N : self.K += 1
        self.edge = [[] for n in range(self.N)]
        self.node = [-1]*self.N
        self.id = []
        self.parent = [[-1]*N for k in range(self.K)]
    def append_edge(self,a,b):
        self.edge[a].append(b)
        self.edge[b].append(a)
    def dfs(self,s):
        stack=[s]
        self.node[s] = 0
        self.parent[0][s] = -1
        while len(stack)>0:
            pos = stack.pop()
            self.id.append(pos)
            for p in self.edge[pos]:
                if self.node[p]==-1:
                    stack.append(p)
                    self.node[p] = self.node[pos]+1
                    self.parent[0][p] = pos
    def doubling(self):
        for k in range(self.K-1):
            for n in range(self.N):
                if self.parent[k][n] == -1 : self.parent[k+1][n] = -1
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
