# distance**2
def distpow(axy,bxy=(0,0)) :
    return (axy[0]-bxy[0])**2 + (axy[1]-bxy[1])**2
# degree
import math
def angleDeg(axy,bxy=(0,0)):
    return math.degrees(math.atan2(axy[1]-bxy[1],axy[0]-bxy[0]))%360
def angleRad(axy,bxy=(0,0)):
    return math.atan2(axy[1]-bxy[1],axy[0]-bxy[0])%(math.pi*2)
# inner product ( <90:innnerP>0, >90:innerP<0, =90:innerP=0 )
def innerP(axy,bxy,cxy=(0,0),dxy=(0,0)) :
    return (axy[0]-cxy[0])*(bxy[0]-dxy[0]) + (axy[1]-cxy[1])*(bxy[1]-dxy[1])
# outer product ( outerP(a,b)>0:ω(a)<ω(b) outerP(a,b)<0:ω(a)>ω(b) outerP(a,b)=0: inline )
# abs(outerP) = area of parallelogram
def outerP(axy,bxy,cxy=(0,0),dxy=(0,0)) :
    return (axy[0]-cxy[0])*(bxy[1]-dxy[1]) - (axy[1]-cxy[1])*(bxy[0]-dxy[0])
# 線分abと線分cdの交差判定
if outerP(axy,dxy,cxy,cxy)==0 and outerP(bxy,dxy,cxy,cxy)==0:
    if max(min(axy[0],bxy[0]),min(cxy[0],dxy[0]))<=min(max(axy[0],bxy[0]),max(cxy[0],dxy[0])) and \
    max(min(axy[1],bxy[1]),min(cxy[1],dxy[1]))<=min(max(axy[1],bxy[1]),max(cxy[1],dxy[1])):
        True
elif outerP(axy,dxy,cxy,cxy)*outerP(bxy,dxy,cxy,cxy)<=0 and outerP(cxy,bxy,axy,axy)*outerP(dxy,bxy,axy,axy)<=0:
    True

# マンハッタン距離、45度回転
for n in range(N) : 
    x,y = map(int,input().split())
    p.append((x-y,x+y))
def getdist(p1,p2):
    return max(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]))

# 最近点対問題(分割統治法)
# 凸包の構築(Andrewのアルゴリズム)
# ボロノイ図(Fortuneのアルゴリズム)
# 美術館問題(多角形の三角形分割)
