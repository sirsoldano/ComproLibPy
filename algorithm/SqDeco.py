# 基本
size = max(1,int(N**0.5))
B = (N+size-1)//size
block = [0]*B
for b in range((x-1)//size):
    # proc
for n in range((x-1)//size*size,x-1):
    # proc

# Mo's algorithm ABC242G ABC293G ABC405G
def Mo_sorted(N,Q,query):
    size = max( 1, int( (N/Q**0.5)*(1.5**0.5) ) )
#    size = int(N/Q**0.5)+1
    mask = (1<<20)-1
    sq = [0]*Q
    for q in range(Q):
        l,r,x = query[q]
        b = (l-1)//size
        if b&1 == 0 : sq[q] = b<<40 | (r-1)<<20 | q
        else : sq[q] = b<<40 | (mask^(r-1))<<20 | q
    sq.sort()
    return [q&mask for q in sq]
for q in Mo_sorted(N,Q,query):
    L,R,x = query[q]
    L-=1;R-=1
    while r<=R:
        # proc
        r+=1
    while l>L :
        l-=1
        # proc
    while r>R+1:
        r-=1
        # proc
    while l<L :
        # proc
        l+=1
    ans[q] = #val
