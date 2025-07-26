# bisect利用
from bisect import bisect_left,bisect
bisect_left(list,num)
min(abs(A[min(N-1,i)]-b),abs(A[max(0,i-1)]-b))

# 右半開
l,r = 0,N+1
while r-l>1:
    m = (l+r)//2
    if not include : l=m
    else : r=m
print(l)
# 競プロ典型#1羊羹 https://atcoder.jp/contests/typical90/submissions/34487062
# ABC269E https://atcoder.jp/contests/abc269/submissions/34951328

# 左半開
l,r = -1,N
while r-l>1:
    m = (l+r)//2
    if include : l = m
    else : r = m
print(r)
# ABC270E https://atcoder.jp/contests/abc270/submissions/35162976

# 高精度sqrt
def sqrt(x):
    l = -1
    r = 10000000000
    while r - 1 > l:
        m = l + (r - l) // 2
        if m * m > x:
            r = m
        else:
            l = m
    return l

# 最長増加部分列(LIS) 狭義ならbl、広義ならbr
a = [*map(int,input().split())]
p,ind_list = [],[0]*N
for n in range(N):
    pi = bl(p,a[n])
    if pi==len(p) : p.append(a[n])
    else : p[pi] = a[n]
    ind_list[n] = pi+1
lis = []
i = len(p)
for n in range(N-1,-1,-1):
    if ind_list[n]==i:
        lis.append(n)
        i-=1
lis.reverse()
print(lis)
