# 階層なしUF木 https://atcoder.jp/contests/typical90/tasks/typical90_l
class UnionFind:
    def __init__(self,n):
        self.uft = [-1]*n
    def find(self,pos):
        if self.uft[pos] == -1 : return pos
        self.uft[pos]=self.find(self.uft[pos])
        return self.uft[pos]
    def union(self,a,b):
        ra,rb = self.find(a),self.find(b)
        if ra!=rb : 
            if self.uft[ra]>self.uft[rb] : ra,rb = rb,ra
            self.uft[ra] += self.uft[rb]
            self.uft[rb] = ra
        return 0
    def same(self,a,b):
        return self.find(a)==self.find(b)

# 最少全域木
items.sort()
ans,cnt=0,0
for c,l,r in items :
    if uf.same(l,r)==False:
        uf.union(l,r)
        ans, cnt = ans+c, cnt+1
if cnt==N : print(ans)
