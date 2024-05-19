# distance**2
def distpow(axy,bxy=(0,0)) : return (axy[0]-bxy[0])**2 + (axy[1]-bxy[1])**2
# degree
import math
def angleDeg(axy,bxy=(0,0)) : return math.degrees(math.atan2(axy[1]-bxy[1],axy[0]-bxy[0]))%360
def angleRad(axy,bxy=(0,0)) : return math.atan2(axy[1]-bxy[1],axy[0]-bxy[0])%(math.pi*2)
# inner product ( <90:innnerP>0, >90:innerP<0, =90:innerP=0 )
def innerP(axy,bxy,cxy=(0,0),dxy=(0,0)) : return (axy[0]-cxy[0])*(bxy[0]-dxy[0]) + (axy[1]-cxy[1])*(bxy[1]-dxy[1])
# outer product ( outerP(a,b)>0:ω(a)<ω(b) outerP(a,b)<0:ω(a)>ω(b) outerP(a,b)=0: inline )
# abs(outerP) = area of parallelogram
def outerP(axy,bxy,cxy=(0,0),dxy=(0,0)) : return (axy[0]-cxy[0])*(bxy[1]-dxy[1]) - (axy[1]-cxy[1])*(bxy[0]-dxy[0])
# 線分abと線分cdの交差判定
if outerP(axy,dxy,cxy,cxy)==0 and outerP(bxy,dxy,cxy,cxy)==0:
    if max(min(axy[0],bxy[0]),min(cxy[0],dxy[0]))<=min(max(axy[0],bxy[0]),max(cxy[0],dxy[0])) and \
    max(min(axy[1],bxy[1]),min(cxy[1],dxy[1]))<=min(max(axy[1],bxy[1]),max(cxy[1],dxy[1])):
        True
elif outerP(axy,dxy,cxy,cxy)*outerP(bxy,dxy,cxy,cxy)<=0 and outerP(cxy,bxy,axy,axy)*outerP(dxy,bxy,axy,axy)<=0:
    True
# 円が接するかの判定
def istouched(cs1,cs2):
    return (cs1[2]+cs2[2])**2>=distpow(cs1[:2],cs2[:2]) and distpow(cs1[:2],cs2[:2])+min(cs1[2],cs2[2])>=max(cs1[2],cs2[2])
# マンハッタン距離、45度回転
for n in range(N) : 
    x,y = map(int,input().split())
    p.append((x-y,x+y))
def getdist(p1,p2):
    return max(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]))

# 三角形の外接円 https://tjkendev.github.io/procon-library/python/geometry/circles_associated_with_triangle.html
def circumcircle(P1, P2, P3):
    x1, y1 = P1; x2, y2 = P2; x3, y3 = P3
    a = 2*(x1 - x2); b = 2*(y1 - y2); p = x1**2 - x2**2 + y1**2 - y2**2
    c = 2*(x1 - x3); d = 2*(y1 - y3); q = x1**2 - x3**2 + y1**2 - y3**2
    det = a*d - b*c
    x = d*p - b*q; y = a*q - c*p
    if det < 0:
        x = -x; y = -y; det = -det
    if det>0 : x /= det; y /= det
    r = ((x - x1)**2 + (y - y1)**2)**.5
    return x, y, r
# いくつかの直線から構成される最大値(最小値)convex_hull
slopes = [] # (minX,a,b) y = ax+b
for n in range(N):
  x,a,b = -1<<60,A[n],B[n]
  while slopes:
    px,pa,pb = slopes[-1]
    x = (pb-b+(a-pa-1))//(a-pa)
    if px < x : break
    slopes.pop()
  slopes.append((x,a,b))
# 凸包 tc:NlogN
def convex_hull(xys):
    cfs, N = [], len(xys)
    for xy in xys:
        while len(cfs)>=2 and outerP(cfs[-1],cfs[-2],xy,xy)>=0 : cfs.pop()
        cfs.append(xy)
    t = len(cfs)
    for xy in xys[N-2::-1]:
        while len(cfs)>=t+1 and outerP(cfs[-1],cfs[-2],xy,xy)>=0 : cfs.pop()
        cfs.append(xy)
    return cfs
# 多角形面積
def polygon_area(xys) : return abs(sum(xys[i-1][0]*xys[i-1][1] - xys[i][1]*xys[i][0] for i in range(len(xys)))) / 2

# 最近点対問題(分割統治法)
# ボロノイ図(Fortuneのアルゴリズム)
# 美術館問題(多角形の三角形分割)
