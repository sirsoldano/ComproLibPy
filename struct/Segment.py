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
# セグメント木
class SegT:
    def __init__(self,N):
        self.slen = 1
        while(self.slen<N) : self.slen<<=1
        self.st = [-1] * (self.slen*2)
    def update(self,i,x):
        i += self.slen
        self.st[i] = x
        while i>=2 :
            i>>=1
            self.st[i] = max(self.st[i*2],self.st[i*2+1])
    def getmax(self,l,r) : return self._getmax(l,r,1,0,self.slen)
    def _getmax(self,l,r,k,tl,tr):
        if l<=tl and tr<=r : return self.st[k]
        elif tr<=l or r<=tl : return -1
        else :
            lc = self._getmax(l,r,k*2,tl,(tl+tr)//2)
            rc = self._getmax(l,r,k*2+1,(tl+tr)//2,tr)
            return max(lc,rc)

# 遅延セグメント木
# 解説 https://algo-logic.info/segment-tree/
# 競プロ典型 https://github.com/E869120/kyopro_educational_90/blob/main/editorial/029-02.jpg
class SegT:
    def __init__(self,N):
        self.slen = 1
        while(self.slen<N) : self.slen<<=1
        self.st = [-1] * (self.slen*2)
        self.lz = [-1] * (self.slen*2)
    def deval(self,k):
        if k < self.slen:
            self.lz[k*2]=max(self.lz[k],self.lz[k*2])
            self.lz[k*2+1]=max(self.lz[k],self.lz[k*2+1])
        self.st[k]=max(self.st[k],self.lz[k])
        self.lz[k]=-1
    def update(self,l,r,h) : return self._update(l,r,h,1,0,self.slen)
    def _update(self,l,r,h,k,tl,tr):
        self.deval(k)
        if l<=tl and tr<=r :
            self.lz[k]=h
            self.deval(k)
            return
        elif tr<=l or r<=tl : return
        else:
            self._update(l,r,h,k*2,tl,(tl+tr)//2)
            self._update(l,r,h,k*2+1,(tl+tr)//2,tr)
            self.st[k] = max(self.st[k*2],self.st[k*2+1])
    def getmax(self,l,r) : return self._getmax(l,r,1,0,self.slen)
    def _getmax(self,l,r,k,tl,tr):
        self.deval(k)
        if l<=tl and tr<=r : return self.st[k]
        elif tr<=l or r<=tl : return -1
        else :
            lc = self._getmax(l,r,k*2,tl,(tl+tr)//2)
            rc = self._getmax(l,r,k*2+1,(tl+tr)//2,tr)
            return max(lc,rc)

# 多重集合
import bisect
class MultiSet:
    # n: サイズ、compress: 座圧対象list-likeを指定(nは無効)
    # multi: マルチセットか通常のOrderedSetか
    def __init__(self, n=0, *, compress=[], multi=True):
        self.multi = multi
        self.inv_compress = sorted(set(compress)) if len(compress) > 0 else [i for i in range(n)]
        self.compress = {k: v for v, k in enumerate(self.inv_compress)}
        self.counter_all = 0
        self.counter = [0] * len(self.inv_compress)
        self.bit = BIT(len(self.inv_compress))

    def add(self, x, n=1):     # O(log n)
        if not self.multi and n != 1: raise KeyError(n)
        x = self.compress[x]
        count = self.counter[x]
        if count == 0 or self.multi:  # multiなら複数カウントできる
            self.bit.add(x + 1, n)
            self.counter_all += n
            self.counter[x] += n

    def remove(self, x, n=1):  # O(log n)
        if not self.multi and n != 1: raise KeyError(n)
        x = self.compress[x]
        count = self.bit.get(x + 1)
        if count < n: raise KeyError(x)
        self.bit.add(x + 1, -n)
        self.counter_all -= n
        self.counter[x] -= n

    def __repr__(self):
        return f'MultiSet {{{(", ".join(map(str, list(self))))}}}'

    def __len__(self):         # oprator len: O(1)
        return self.counter_all

    def count(self, x):        # O(1)
        return self.counter[self.compress[x]] if x in self.compress else 0

    def __getitem__(self, i):  # operator []: O(log n)
        if i < 0: i += len(self)
        x = self.bit.lower_bound(i + 1)
        if x > self.bit.n: raise IndexError('list index out of range')
        return self.inv_compress[x - 1]

    def __contains__(self, x): # operator in: O(1)
        return self.count(x) > 0

    def bisect_left(self, x):  # O(log n)
        return self.bit.sum(bisect.bisect_left(self.inv_compress, x))

    def bisect_right(self, x): # O(log n)
        return self.bit.sum(bisect.bisect_right(self.inv_compress, x))

class BIT:
    def __init__(self, n):
        self.n = len(n) if isinstance(n, list) else n
        self.size = 1 << (self.n - 1).bit_length()
        if isinstance(n, list):  # nは1-indexedなリスト
            a = [0]
            for p in n: a.append(p + a[-1])
            a += [a[-1]] * (self.size - self.n)
            self.d = [a[p] - a[p - (p & -p)] for p in range(self.size + 1)]
        else:                    # nは大きさ
            self.d = [0] * (self.size + 1)

    def __repr__(self):
        p = self.size
        res = []
        while p > 0:
            res2 = []
            for r in range(p, self.size + 1, p * 2):
                l = r - (r & -r) + 1
                res2.append(f'[{l}, {r}]:{self.d[r]}')
            res.append(' '.join(res2))
            p >>= 1
        res.append(f'{[self.sum(p + 1) - self.sum(p) for p in range(self.size)]}')
        return '\n'.join(res)

    def add(self, p, x):  # O(log(n)), 点pにxを加算
        assert p > 0
        while p <= self.size:
            self.d[p] += x
            p += p & -p

    def get(self, p, default=None):     # O(log(n))
        assert p > 0
        return self.sum(p) - self.sum(p - 1) if 1 <= p <= self.n or default is None else default

    def sum(self, p):     # O(log(n)), 閉区間[1, p]の累積和
        assert p >= 0
        res = 0
        while p > 0:
            res += self.d[p]
            p -= p & -p
        return res

    def lower_bound(self, x):   # O(log(n)), x <= 閉区間[1, p]の累積和 となる最小のp
        if x <= 0: return 0
        p, r = 0, self.size
        while r > 0:
            if p + r <= self.n and self.d[p + r] < x:
                x -= self.d[p + r]
                p += r
            r >>= 1
        return p + 1
