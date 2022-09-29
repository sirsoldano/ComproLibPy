# フェニック木(BinaryIndexedTree)
# 解説 https://qiita.com/R_olldIce/items/f2f7930e7f67963f0493
# 競プロ典型 https://github.com/E869120/kyopro_educational_90/blob/main/editorial/017-03.jpg
class fenT:
    def __init__(self,N):
        self.fen=[0]*(N+1)
    def add(self,n):
        while n<=len(self.fen)-1:
            self.fen[n]+=1
            n += n&-n
    def query(self,n):
        ans = 0
        while n>0:
            ans += self.fen[n]
            n -= n&-n
        return ans

# セグメント木
# 解説 https://algo-logic.info/segment-tree/
# 競プロ典型 https://github.com/E869120/kyopro_educational_90/blob/main/editorial/029-02.jpg
import sys
sys.setrecursionlimit(100000)
class segT:
    def __init__(self,N):
        self.slen = 1
        while(self.slen<N) : self.slen<<=1
        self.st = [0] * (self.slen*2)
        self.lz = [0] * (self.slen*2)
    def deval(self,k):
        if k < self.slen:
            self.lz[k*2]=max(self.lz[k],self.lz[k*2])
            self.lz[k*2+1]=max(self.lz[k],self.lz[k*2+1])
        self.st[k]=max(self.st[k],self.lz[k])
        self.lz[k]=0
    def update(self,l,r,h,k,tl,tr):
        self.deval(k)
        if tr<=l or r<=tl : return
        if l<=tl and tr<=r :
            self.lz[k]=h
            self.deval(k)
            return
        self.update(l,r,h,k*2,tl,(tl+tr)//2)
        self.update(l,r,h,k*2+1,(tl+tr)//2,tr)
        self.st[k] = max(self.st[k*2],self.st[k*2+1])
    def getmax(self,l,r,k,tl,tr):
        self.deval(k)
        if tr<=l or r<=tl : return 0
        elif l<=tl and tr<=r : return self.st[k]
        else :
            lc = self.getmax(l,r,k*2,tl,(tl+tr)//2)
            rc = self.getmax(l,r,k*2+1,(tl+tr)//2,tr)
            return max(lc,rc)

