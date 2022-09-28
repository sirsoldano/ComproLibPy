# 漸化式のように、小さい問題の結果を利用して解くアルゴリズム
# ナップザック問題 https://atcoder.jp/contests/math-and-algorithm/tasks/dp_d
# tc : N*W
N,W = map(int,input().split())
dp = [[-1]*(W+1) for n in range(N+1)]
dp[0][0]=0
for n in range(1,N+1):
    wei,val = map(int,input().split())
    for w in range(W+1):
        dp[n][w] = dp[n-1][w]
        if w-wei>=0 and dp[n-1][w-wei]>=0:
            dp[n][w] = max(dp[n][w],dp[n-1][w-wei]+val)

# 桁DP https://github.com/E869120/kyopro_educational_90/blob/main/editorial/005-01.jpg
N,B,K = map(int,input().split()) # N:桁数、B:因数、K:Cの個数
C = list(map(int,input().split())) # 構成する数字
dp = [[0]*B for n in range(N+1)]
dp[0][0]=1
for n in range(N):
    for b in range(B):
        for k in range(K):
            dp[n+1][(10*b+C[k])%B] += dp[n][b]
            dp[n+1][(10*b+C[k])%B] %= 1000000007
print(dp[N][0])
# 桁DPは行列化して繰り返し二乗法を利用可能

# 部分集合の場合の数は状態DP https://github.com/E869120/kyopro_educational_90/blob/main/editorial/008.jpg
# dp[全体集合の何文字目][部分集合の何文字目]
dp = [[0]*7 for n in range(len(S)+1)]
for n in range(1,len(S)+1):
    for i in range(7) : dp[n][i]=dp[n-1][i]
    if S[n-1]==0 : dp[n][0]=1+dp[n-1][0]
    else : dp[n][S[n-1]] = (dp[n][S[n-1]]+dp[n-1][S[n-1]-1])%1000000007

# 数列操作は区間DP https://github.com/E869120/kyopro_educational_90/blob/main/editorial/019.jpg
dp = [[100000000000000000]*2*N for n in range(2*N-1)]
for l in range(2*N-1) : dp[l][l+1] = abs(A[l+1]-A[l])
for n in range(3,2*N,2):
    for l in range(2*N-n):
        dp[l][l+n] = dp[l+1][l+n-1]+abs(A[l]-A[l+n])
        for m in range(l+1,l+n-1) : dp[l][l+n] = min(dp[l][l+n],dp[l][m]+dp[m+1][l+n])
print(dp[0][2*N-1])
# 部分和問題、コイン問題、編集距離、重み付き区間スケジューリング、巡回セールスマン
