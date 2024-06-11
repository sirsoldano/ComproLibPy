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
from math import gcd
class SegT:
    DEFAULT = {
        'min': 1 << 60, 'max': -(1 << 60), 'sum': 0,
        'prd': 1, 'gcd': 0, 'lmc': 1,
        '^': 0, '&': (1 << 60) - 1, '|': 0,
    }
    FUNC = {
        'min': min, 'max': max, 'sum': (lambda x, y: x + y),
        'prd': (lambda x, y: x * y), 'gcd': gcd, 'lmc': (lambda x, y: (x * y) // gcd(x, y)),
        '^': (lambda x, y: x ^ y), '&': (lambda x, y: x & y), '|': (lambda x, y: x | y),
    }
    def __init__(self,N,mode="max",func=None,default=None):
        self.default = self.DEFAULT[mode] if default == None else default
        self.func = self.FUNC[mode] if func == None else func
        self.slen = 1
        while(self.slen<N) : self.slen<<=1
        self.st = [self.default] * (self.slen*2)
    def update(self,i,x):
        i += self.slen
        self.st[i] = x
        while i>=2 :
            i>>=1
            self.st[i] = self.func(self.st[i*2],self.st[i*2+1])
    def get(self,l,r):
        l += self.slen; r += self.slen
        res = self.default
        while l < r:
            if l & 1 : 
                res = self.func(res, self.st[l])
                l += 1
            if r & 1: 
                r -= 1 
                res = self.func(res, self.st[r])
            l >>= 1; r >>= 1
        return res
# 遅延セグメント木
# 解説 https://qiita.com/Kept1994/items/a3435f50951e6b46709e
# 競プロ典型 https://github.com/E869120/kyopro_educational_90/blob/main/editorial/029-02.jpg
from math import gcd
class LST:
    DEFAULT = {
        'min': 1 << 60, 'max': -(1 << 60), 'sum': 0,
        'prd': 1, 'gcd': 0, 'lmc': 1,
        '^': 0, '&': (1 << 60) - 1, '|': 0, None: None
    }
    FUNC = {
        'min': min, 'max': max, 'sum': (lambda x, y: x + y),
        'prd': (lambda x, y: x * y), 'gcd': gcd, 'lmc': (lambda x, y: (x * y) // gcd(x, y)),
        '^': (lambda x, y: x ^ y), '&': (lambda x, y: x & y), '|': (lambda x, y: x | y),
    }
    def __init__(self,N,mode="max",upfunc=None,dnfunc=None,default=None):
        self.default = self.DEFAULT[mode] if default == None else default
        self.upfunc = self.FUNC[mode] if upfunc == None else self.FUNC[upfunc] if type(upfunc) is str else upfunc
        self.dnfunc = self.FUNC[mode] if dnfunc == None else self.FUNC[dnfunc] if type(dnfunc) is str else dnfunc
        self.st = [self.default for _ in range(1<<(N.bit_length()+1))]
        self.base = len(self.st)>>1
        self.lz = [self.default for _ in range(self.base)]
    def _apply(self,k,h):
        self.st[k] = self.dnfunc(self.st[k],h)
        if k<self.base : self.lz[k] = self.dnfunc(self.lz[k],h)
    def _eval(self,k):
        while k>1:
            k>>=1
            self.st[k] = self.upfunc(self.st[k*2],self.st[k*2+1])
            if self.lz[k] != self.default : self.st[k] = self.dnfunc(self.st[k],self.lz[k])
    def _deval(self,i):
        for b in reversed(range(1,i.bit_length())):
            k = i>>b
            if self.lz[k] == self.default:continue
            self._apply(k*2,self.lz[k])
            self._apply(k*2+1,self.lz[k])
            self.lz[k] = self.default
    def update(self,l,r,h):
        l += self.base; r += self.base
        l0,r0 = l,r-1
        self._deval(l0); self._deval(r0)
        while l < r:
            if l & 1 : 
                self._apply(l,h)
                l += 1
            if r & 1: 
                r -= 1 
                self._apply(r,h)
            l >>= 1; r >>= 1
        self._eval(l0); self._eval(r0)
    def get(self,l,r):
        l += self.base; r += self.base
        res = self.default
        self._deval(l); self._deval(r-1)
        while l < r:
            if l & 1 : 
                res = self.upfunc(res,self.st[l])
                l += 1
            if r & 1: 
                r -= 1 
                res = self.upfunc(res,self.st[r])
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

# 長方形の和集合の面積 https://atcoder.jp/contests/abc346/tasks/abc346_g
def op(mon1,mon2) : 
  if mon1[0]<mon2[0] : return mon1
  elif mon1[0]>mon2[0] : return mon2
  else : return mon1[0],mon1[1]+mon2[1]
def mp(act,mon) : return mon[0]+act,mon[1]
def comp(act1,act2) : return act1+act2
lst = LazySegTree(op,(0,0),mp,comp,0,[(0,1) for n in range(N+1)])
ans = 0
for n in range(N+1):
  for und,ovr in lef[n]:
    lst.apply(und,ovr+1,1)
  mn,con = lst.prod(0,N+1)
  ans += N+1-con*(mn==0)
  for und,ovr in rig[n]:
    lst.apply(und,ovr+1,-1)
print(ans)

# 長方形の一番厚く重なっている点の高さ https://atcoder.jp/contests/abc327/tasks/abc327_f
def op(s1,s2) : return max(s1,s2)
def mp(f,s) : return s+f
def comp(f1,f2) : return f1+f2
lst = LazySegTree(op,0,mp,comp,0,[0 for n in range(200001)])
ans = 0
for n in range(200001):
  for und,ovr in lef[n]:
    lst.apply(und,ovr+1,1)
  ans = max(ans,lst.all_prod())
  for und,ovr in rig[n]:
    lst.apply(und,ovr+1,-1)
print(ans)

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

# 2Dセグメント木
class SegT2d:
    def __init__(self,H,W):
        self.hlen,self.wlen = 1,1
        while(self.hlen<H) : self.hlen<<=1
        while(self.wlen<W) : self.wlen<<=1
        self.st = [[-1<<60]*(self.wlen*2) for _ in range(self.hlen*2)]
    def update(self,h,w,x):
        h += self.hlen; w += self.wlen
        self.st[h][w] = x
        while True:
            tw = w
            while tw>1:
                tw >>= 1
                self.st[h][tw] = max(self.st[h][tw*2],self.st[h][tw*2+1])
            h>>=1
            if h==0 : break
            self.st[h][w] = max(self.st[h*2][w],self.st[h*2+1][w])
    def getmax(self,hl,hr,wl,wr):
        hl += self.hlen; hr += self.hlen
        wl += self.wlen; wr += self.wlen
        res = -1<<60
        while hl < hr:
            if hl & 1 :
                twl,twr = wl,wr
                while twl<twr:
                    if twl&1:
                        res = max(res,self.st[hl][twl])
                        twl+=1
                    if twr&1:
                        twr-=1
                        res = max(res,self.st[hl][twr])
                    twl>>=1;twr>>=1
                hl += 1
            if hr & 1: 
                hr -= 1 
                twl,twr = wl,wr
                while twl<twr:
                    if twl&1:
                        res = max(res,self.st[hr][twl])
                        twl+=1
                    if twr&1:
                        twr-=1
                        res = max(res,self.st[hr][twr])
                    twl>>=1;twr>>=1
            hl >>= 1; hr >>= 1
        return res

# (編集途中)
class SegT:
    def __init__(self,H,W):
        self.hlen,self.wlen = 1,1
        while(self.hlen<H) : self.hlen<<=1
        while(self.wlen<W) : self.wlen<<=1
        self.st = [[1<<60]*(self.wlen*2) for _ in range(self.hlen*2)]
        self.lz = [[1<<60]*(self.wlen*2) for _ in range(self.hlen*2)]
    def eval(self,h,w):
        while True:
            tw = w
            while tw>1:
                tw >>= 1
                self.st[h][tw] = min(self.st[h][tw*2],self.st[h][tw*2+1])
            h >>= 1
            if h==0 : break
            self.st[h][w] = min(self.st[h*2][w],self.st[h*2+1][w])
    def deval(self,h,w):
        th, dh = 1, 1
        tw, dw = 1, 1
        while dh*4<=h : dh*=2
        while dw*4<=w : dw*=2
        while th <= h :
            while tw <= w:
                
            if k < self.slen:
                self.lz[k*2] = max(self.lz[k*2],self.lz[k])
                self.lz[k*2+1] = max(self.lz[k*2+1],self.lz[k])
            self.st[k] = max(self.st[k],self.lz[k])
            self.lz[k] = 0
            if i&d : k = k*2+1
            else : k = k*2
            d >>= 1
    def update(self,hl,hr,wl,wr,h):
        hl += self.hlen; hr += self.hlen
        wl += self.wlen; wr += self.wlen
        while hl < hr:
            if hl & 1 : 
                twl,twr = wl,wr
                while twl<twr:
                    if twl&1:
                        self.deval(hl,twl)
                        self.lz[hl][twl] = min(self.lz[hl][twl],h)
                        self.st[hl][twl] = min(self.st[hl][twl],h)
                        self.eval(hl,twl)
                        twl+=1
                    if twr&1:
                        twr-=1
                        self.deval(hl,twr)
                        self.lz[hl][twr] = min(self.lz[hl][twr],h)
                        self.st[hl][twr] = min(self.st[hl][twr],h)
                        self.eval(hl,twr)
                    twl>>=1 ; twr>>=1
                hl += 1
            if hr & 1: 
                hr -= 1
                twl,twr = wl,wr
                while twl<twr:
                    if twl&1:
                        self.deval(hr,twl)
                        self.lz[hr][twl] = min(self.lz[hr][twl],h)
                        self.st[hr][twl] = min(self.st[hr][twl],h)
                        self.eval(hr,twl)
                        twl+=1
                    if twr&1:
                        twr-=1
                        self.deval(hr,twr)
                        self.lz[hr][twr] = min(self.lz[hr][twr],h)
                        self.st[hr][twr] = min(self.st[hr][twr],h)
                        self.eval(hr,twr)
                    twl>>=1 ; twr>>=1
            hl >>= 1; hr >>= 1
    def getmin(self,l,r):
        l += self.slen; r += self.slen
        res = 1<<60
        while l < r:
            if l & 1 : 
                res = min(res,self.st[l])
                l += 1
            if r & 1: 
                r -= 1 
                res = min(res,self.st[r])
            l >>= 1; r >>= 1
        return res
