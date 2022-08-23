# 漸化式のように、小さい問題の結果を利用して解くアルゴリズム
# napsack https://atcoder.jp/contests/math-and-algorithm/tasks/dp_d
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

# 部分和問題、コイン問題、編集距離、重み付き区間スケジューリング、巡回セールスマン
