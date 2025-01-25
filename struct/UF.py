# 階層なしUF木 https://atcoder.jp/contests/typical90/tasks/typical90_l
import sys; sys.setrecursionlimit(10**6); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
class UnionFind:
    def __init__(self,N):
        self.uft = [n for n in range(N)]
        self.rank = [0]*N
    def root(self,pos):
        if self.uft[pos] == pos : return pos
        self.uft[pos]=self.root(self.uft[pos])
        return self.uft[pos]
    def union(self,a,b):
        ra,rb = self.root(a),self.root(b)
        if ra==rb : return
        if self.rank[ra] < self.rank[rb] :
            self.uft[ra] = rb
        else :
            self.uft[rb] = ra
            if self.rank[ra]==self.rank[rb] : self.rank[ra]+=1
    def same(self,a,b):
        return self.root(a)==self.root(b)

# 最少全域木 (クラスカル法)
items.sort()
ans,cnt=0,0
for c,l,r in items :
    if uf.same(l,r)==False:
        uf.union(l,r)
        ans, cnt = ans+c, cnt+1
if cnt==N-1 : print(ans)

# heapq ver
import heapq as hq
ans,cnt=0,1
uf = UnionFind(N)
while e:
    c,l,r=hq.heappop(e)
    if uf.same(l,r)==False:
        uf.union(l,r)
        ans, cnt = ans+c, cnt+1
if cnt==N : print(ans)
else : print(-1)
