# 階層なしUF木 https://atcoder.jp/contests/typical90/tasks/typical90_l
import sys
sys.setrecursionlimit(10**6)
class UnionFind:
    def __init__(self,n):
        self.uft = [-1]*n
        self.rank = [0]*n
    def root(self,pos):
        if self.uft[pos] == -1 : return pos
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

# 最少全域木
items.sort()
ans,cnt=0,0
for c,l,r in items :
    if uf.same(l,r)==False:
        uf.union(l,r)
        ans, cnt = ans+c, cnt+1
if cnt==N : print(ans)
