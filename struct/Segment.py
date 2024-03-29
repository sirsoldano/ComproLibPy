# フェニック木(BinaryIndexedTree)
# 解説 https://qiita.com/R_olldIce/items/f2f7930e7f67963f0493
# 競プロ典型 https://github.com/E869120/kyopro_educational_90/blob/main/editorial/017-03.jpg
class FenT:
    def __init__(self,N):
        self.tree=[0]*(N+1)
    def add(self,n,i):
        while n<=len(self.tree)-1:
            self.tree[n]+=i
            n += n&-n
    def sum(self,l,r):
        return self._sum(r)-self._sum(l)
    def _sum(self,n):
        ans = 0
        while n>0:
            ans += self.tree[n]
            n -= n&-n
        return ans
    def binsearch(self,n):
        l,r=0,len(self.tree)+1
        while r-l>1:
            m=(l+r)//2
            if self._sum(m)>=n:
                r=m
            else:
                l=m
        return l
    def lower_bound(self,n):
        l,r=0,len(self.tree)
        n=self._sum(n)+1
        while r-l>1:
            m=(l+r)//2
            if self._sum(m)>=n:
                r=m
            else:
                l=m
        return r
# セグメント木
class SegT:
    def __init__(self,N):
        self.slen = 1
        while(self.slen<N) : self.slen<<=1
        self.st = [0] * (self.slen*2)
    def update(self,i,x):
        i += self.slen
        self.st[i] = x
        while i>=2 :
            i>>=1
            self.st[i] = max(self.st[i*2],self.st[i*2+1])
#            self.st[i] = self.st[i*2]+self.st[i*2+1]
    def getmax(self,l,r):
#    def getsum(self,l,r):
        l += self.slen; r += self.slen
        res = 0
        while l < r:
            if l & 1 : 
                res = max(res, self.st[l])
#                res += self.st[l]
                l += 1
            if r & 1: 
                r -= 1 
                res = max(res, self.st[r])
#                res += self.st[r]
            l >>= 1; r >>= 1
        return res
# 遅延セグメント木
# 解説 https://qiita.com/Kept1994/items/a3435f50951e6b46709e
# 競プロ典型 https://github.com/E869120/kyopro_educational_90/blob/main/editorial/029-02.jpg
class SegT:
    def __init__(self,N):
        self.slen = 1
        while(self.slen<N) : self.slen<<=1
        self.st = [0] * (self.slen*2)
        self.lz = [0] * (self.slen*2)
    def eval(self,k):
        while k>0:
            self.st[k] = max(self.st[k*2],self.st[k*2+1])
            k>>=1
    def deval(self,i):
        k, d = 1, 1
        while d*4<=i:d*=2
        while k <= i :
            if k < self.slen:
                self.lz[k*2] = max(self.lz[k*2],self.lz[k])
#                self.lz[k*2] += self.lz[k]
                self.lz[k*2+1] = max(self.lz[k*2+1],self.lz[k])
#                self.lz[k*2+1] += self.lz[k]
            self.st[k] = max(self.st[k],self.lz[k])
#            self.st[k] += self.lz[k]
            self.lz[k] = 0
            if i&d : k = k*2+1
            else : k = k*2
            d >>= 1
    def update(self,l,r,h):
        l += self.slen; r += self.slen
        while l < r:
            if l & 1 : 
                self.deval(l)
                self.lz[l] = max(self.lz[l],h)
#                self.lz[l] += h
                self.st[l] = max(self.st[l],h)
                self.eval(l>>1)
                l += 1
            if r & 1: 
                r -= 1 
                self.deval(r)
                self.lz[r] = max(self.lz[r],h)
#                self.lz[r] += h
                self.st[r] = max(self.st[r],h)
                self.eval(r>>1)
            l >>= 1; r >>= 1
    def getmax(self,l,r):
        l += self.slen; r += self.slen
        res = 0
        while l < r:
            if l & 1 : 
                self.deval(l)
                res = max(res,self.st[l])
                l += 1
            if r & 1: 
                r -= 1 
                self.deval(r)
                res = max(res,self.st[r])
            l >>= 1; r >>= 1
        return res
# atcoder library
# 解説 https://qiita.com/hyouchun/items/1748bd320d2188a999f2
# 例題 https://atcoder.jp/contests/abc327/submissions/47323870
from atcoder.lazysegtree import LazySegTree
lst = LazySegTree(max, 0, lambda f, x: f + x, lambda f, g: f + g, 0, [0] * mx )
lst.apply(l,r,1)
ans = max(ans,lst.all_prod())
# 漸化式を伴うもの https://atcoder.jp/contests/abc332/submissions/48482067

# セグメント木＋ローリングハッシュ
class SegT:
    def __init__(self,N):
        self.slen = 1
        self.p = 1000000007
        self.x = [998244353,100000007]
        self.xpow = [[1 for n in range(N+1)],[1 for n in range(N+1)]]
        for n in range(N) : 
            self.xpow[0][n+1] = (self.xpow[0][n]*self.x[0])%self.p
            self.xpow[1][n+1] = (self.xpow[1][n]*self.x[1])%self.p
        while(self.slen<N) : self.slen<<=1
        self.st = [[0] * (self.slen*2), [0] * (self.slen*2)]
    def update(self,i,s):
        i += self.slen
        self.st[0][i],self.st[1][i] = s,s
        l=1
        while i>=2 :
            i>>=1
            self.st[0][i] = (self.st[0][i*2]*self.xpow[0][l]+self.st[0][i*2+1])%self.p
            self.st[1][i] = (self.st[1][i*2]*self.xpow[1][l]+self.st[1][i*2+1])%self.p
            l<<=1
    def gethash(self,l,r) : return self._gethash(l,r,1,0,self.slen)
    def _gethash(self,l,r,k,tl,tr):
        if l<=tl and tr<=r : return [self.st[0][k],self.st[1][k]]
        elif tr<=l or r<=tl : return [0,0]
        else :
            lc = self._gethash(l,r,k*2,tl,(tl+tr)//2)
            rc = self._gethash(l,r,k*2+1,(tl+tr)//2,tr)
            return [(lc[0]*self.xpow[0][max(0,min(r,tr)-(tl+tr)//2)]+rc[0])%self.p,(lc[1]*self.xpow[1][max(0,min(r,tr)-(tl+tr)//2)]+rc[1])%self.p]
ft.SegT(N+1); for n in range(N) : ft.update(n+1,s[n]); ft.gethash(l,r+1)

# マージソート木
from heapq import merge
from bisect import bisect as br
class MergeT:
    def __init__(self,N,A):
        self.slen = 1
        while(self.slen<N) : self.slen<<=1
        self.st = [[] for i in range(self.slen*2)]
        self.scs = [[] for i in range(self.slen*2)]
        for n in range(N):
            self.st[self.slen+n] = [A[n]]
            self.scs[self.slen+n] = [0,A[n]]
        for i in range(self.slen-1,0,-1):
            *self.st[i], = merge(self.st[i*2],self.st[i*2+1])
            self.scs[i] = self.cs(self.st[i])
    def cs(self,l):
        lsum = [0]
        for n in range(len(l)) : lsum.append(lsum[-1]+l[n])
        return lsum
    def getsum(self,l,r,hi,lo=0):
        l += self.slen; r += self.slen
        res = 0
        while l < r:
            if l & 1 : 
                res += self.scs[l][br(self.st[l],hi)]
                l += 1
            if r & 1: 
                r -= 1 
                res += self.scs[r][br(self.st[r],hi)]
            l >>= 1; r >>= 1
        return res
