# Floor Difference
def fd(A):
    return [A[0]]+[A[n]-A[n-1] for n in range(1,len(A))]

# Cumulative Sum
def cs(A):
    N = len(A)
    csum = [A[0]]+[0]*(N-1)
    for n in range(1,N) : csum[n] = csum[n-1] + A[n]
    return csum

# CS2d
cs = [[0]*(N+1) for n in range(N+1)]
for l in range(1,N+1):
    for r in range(1,N+1) : cs[l][r]+=cs[l][r-1] + a[l-1][r-1]
    for r in range(1,N+1) : cs[l][r]+=cs[l-1][r]
def getsum(cs,lh,lw,rh,rw) : return cs[rh][rw]-cs[rh][lw-1]-cs[lh-1][rw]+cs[lh-1][lw-1]

psum = [[0]*(N+1) for n in range(N+1)]
for n in range(N):
    for m in range(N):
        psum[n+1][m+1] = p[n][m]+psum[n+1][m]+psum[n][m+1]-psum[n][m]
# https://atcoder.jp/contests/abc106/tasks/abc106_d
# https://atcoder.jp/contests/abc331/tasks/abc331_d
# 領域追加は二次元いもす法 https://github.com/E869120/kyopro_educational_90/blob/main/editorial/028.jpg
