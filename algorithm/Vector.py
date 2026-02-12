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
# 点と線分の最短距離
def distance_point_to_segment(p1, p2, p = (0,0)):
    px, py = p
    x1, y1 = p1
    x2, y2 = p2
    # 線分ベクトルの成分
    vec_x = x2 - x1
    vec_y = y2 - y1
    # 線分の長さの2乗を計算
    length_squared = vec_x**2 + vec_y**2
    # 線分が点である場合（端点1と2が同じ座標）
    if length_squared == 0 : return sqrt((px - x1)**2 + (py - y1)**2)
    # 点pが線分のどの位置に射影されるかを計算する
    # t = ((p - p1)・(p2 - p1)) / |p2 - p1|^2
    t = ((px - x1) * vec_x + (py - y1) * vec_y) / length_squared
    # 射影点が線分の外側 (p1側) にある場合
    if t < 0 : return sqrt((px - x1)**2 + (py - y1)**2)
    # 射影点が線分の外側 (p2側) にある場合
    elif t > 1 : return sqrt((px - x2)**2 + (py - y2)**2)
    # 射影点が線分上にある場合 (0 <= t <= 1)
    else:
        # 垂線の足(射影点)の座標を計算
        projection_x = x1 + t * vec_x
        projection_y = y1 + t * vec_y
        # 点pと射影点の距離が最短となる
        return sqrt((px - projection_x)**2 + (py - projection_y)**2)
# 円が接するかの判定
def istouched(cs1,cs2):
    return (cs1[2]+cs2[2])**2>=distpow(cs1[:2],cs2[:2]) and distpow(cs1[:2],cs2[:2])+min(cs1[2],cs2[2])>=max(cs1[2],cs2[2])
# マンハッタン距離、45度回転
for n in range(N) : 
    x,y = map(int,input().split())
    p.append((x-y,x+y))
def getdist(p1,p2):
    return max(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]))

# 偏角ソート https://atcoder.jp/contests/abc442/tasks/abc442_e
class Arg:
    def __init__ (self, x, y, n):
        self.x , self.y, self.n = x , y, n
    def __lt__ (self, other):
        return arg_sort(self,other)<=0
def arg_sort(p0, p1):
    x0, y0 = p0.x,p0.y
    x1, y1 = p1.x,p1.y
    h0 = y0<0 or (y0==0 and x0<0)
    h1 = y1<0 or (y1==0 and x1<0)
    if h0!=h1 : return 1 if h0<h1 else -1
    return 1 if x0*y1-y0*x1>0 else 0 if x0*y1-y0*x1==0 else -1
N = int(input())
xy = [Arg(*([*map(int,input().split())]+[n])) for n in range(N)]
xys = sorted(xy)

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
# いくつかの直線から構成される最大値(最小値) convex_hull
# https://atcoder.jp/contests/abc289/tasks/abc289_g
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
convex_hull(sorted(xys))
# 多角形面積
def polygon_area(xys) : return abs(sum(xys[i-1][0]*xys[i-1][1] - xys[i][1]*xys[i][0] for i in range(len(xys)))) / 2

# 最近点対問題(分割統治法)
# ボロノイ図(Fortuneのアルゴリズム)
# 美術館問題(多角形の三角形分割)
