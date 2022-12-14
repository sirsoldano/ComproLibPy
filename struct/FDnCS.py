# Floor Difference
def fd(A):
    return [A[0]]+[A[n]-A[n-1] for n in range(1,len(A))]

# Cumulative Sum
def cs(A):
    N = len(A)
    CS = [A[0]]+[0]*(N-1)
    for n in range(1,N) : CS[n] = CS[n-1] + A[n]
    return CS

# 領域追加は二次元いもす法 https://github.com/E869120/kyopro_educational_90/blob/main/editorial/028.jpg
