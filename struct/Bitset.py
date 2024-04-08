class Bitset:
    def __init__(self,N,A=None):
        self.base = 63
        self.bs = [0]*(N//self.base+1)
        if A:
            for i in range(len(self.bs)):
                sum((1<<b)*A[n][b+i*self.base] for b in range(self.base) if b+i*self.base<N)
    def add(self,i):
        self.bs[i//self.base] += 1<<(i%self.base)
    def rm(self,i):
        self.bs[i//self.base] -= 1<<(i%self.base)
    def xor(self,bsa):
        for i in range(len(self.bs)):
            self.bs[i] ^= bsa[i]
    def cnt(self):
        return sum(self.popcnt(self.bs[i]) for i in range(len(self.bs)))
    def popcnt(self,x):
        x = x - ((x >> 1) & 0x5555555555555555)
        x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
        x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
        x += (x >> 8)
        x += (x >> 16)
        x += (x >> 32)
        return x & 0x0000007f
