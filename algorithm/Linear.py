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
    def modpowL(self,a,p,ans=None):
        if ans is None : ans = [[1 if m==n else 0 for m in range(len(a))] for n in range(len(a))]
        for i in range(len(a)):
            for k in range(len(a)):
                for j in range(len(a)):
                    c[i][j] = (c[i][j]+a[i][k]*b[k][j])%self.mod
        return c
