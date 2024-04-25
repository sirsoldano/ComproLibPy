class Linear:
    def __init__(self,mod):
        self.mod = mod
    def modpowL(self,a,p):
        ans = [[1 if m==n else 0 for m in range(len(a))] for n in range(len(a))]
        while p>0:
            if p&1 : ans = self.mulmodL(ans,a)
            p>>=1
            a = self.mulmodL(a,a)
        return ans
    def mulmodL(self,a,b):
        c = [[0 for m in range(len(b[0]))] for n in range(len(a))]
        for i in range(len(a)):
            for k in range(len(a)):
                for j in range(len(b[0])):
                    c[i][j] = (c[i][j]+a[i][k]*b[k][j])%self.mod
        return c
    def sumL(self,a):
        return sum(sum(a[r][c]for c in range(len(a[0])) )%self.mod for r in range(len(a)))%self.mod
lin.sumL( lin.mulmodL( lin.modpowL(coef,N) , [*zip(A)] ) )

def matexp(a,r,b,mod): # a^r * b
    n = len(a); m = r.bit_length()
    res = [a]+[[[0]*n for _ in range(n)] for _ in range(m-1)]
    for h in range(m-1):
        for i in range(n):
            for j in range(n):
                for k in range(n): res[h+1][i][j] += res[h][i][k]*res[h][k][j]%mod
                res[h+1][i][j] %= mod
    for h in range(m):
        if not r>>h&1: continue
        tmp = [0]*n
        for i in range(n):
            for j in range(n): tmp[i] += res[h][i][j]*b[j]%mod
            tmp[i] %= mod
        b = tmp
    return b
