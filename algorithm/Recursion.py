# 分割統治法
def DivCon(l,r) :
    if r-l==1 : return A[l]
    m = (l+r)//2
    return divcon(l,m)+divcon(m,r)

# マージソート
# tc : NlogN
# ul : 10^6
def MergeSort(l,r) :
    if r-l==1 : return
    m = (l+r)//2
    MergeSort(l,m); MergeSort(m,r)
    ordered,c1,c2,cnt = [0]*(r-l),l,m,0
    while c1<m or c2<r :
        if c1==m or ( c2<r and A[c2]<=A[c1] ):
            ordered[cnt] = A[c2]
            c2+=1
        else:
            ordered[cnt] = A[c1]
            c1+=1
        cnt+=1
    for c in range(cnt) : A[l+c]=ordered[c]

#自然数の和の組み合わせ列挙
def addCombinations(nums, i, total, sum_left):
    prev_num = nums[i - 1] if (i > 0) else 1
    for k in range(prev_num, total + 1):
        nums[i] = k
        if sum_left > k and i+1<total : addCombinations(nums, i + 1, total, sum_left - k)
        if sum_left == k : combs.add(tuple(nums[:i+1]+[0]*(total-i-1)))
combs = set()
addCombinations([0]*betn,0,betn,unbn)
for comb in combs:
    for perm in set(permutations(comb)):
