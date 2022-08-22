# fast combination
# ul : 100
for a in range(N-4):
    for b in range(a+1,N-3):
        for c in range(b+1,N-2):
            for d in range(c+1,N-1):
                for e in range(d+1,N):

# 少ないパターンの側に着目し数え上げる
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_v

# 全出現までの回数期待値 r枚出現時 : (r/N)^0+(r/N)^1+(r/N)^2+(r/N)^3+... = N/(N-r)
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_z
