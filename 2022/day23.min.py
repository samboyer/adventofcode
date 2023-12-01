F=open('i/23').readlines();R=range;E=[(x,y)for y in R(len(F))for x in R(len(F[-1]))if F[y][x]=='#']
for r in R(10):
 P={};Q={}
 for x,y in E:
  d=(x,y);A=*zip([x-1,x,x+1]*3,[y-1]*3+[y]*3+[y+1]*3),
  for o in '1'+['NSWE','SWEN','WENS','ENSW'][r%4]+'0':
   if all(a==4 or A[a]not in E for a in{'N':(0,1,2),'S':(6,7,8),'W':(0,3,6),'E':(2,5,8),'0':(),'1':R(9)}[o]):c={'N':A[1],'S':A[7],'W':A[3],'E':A[5],'0':d,'1':d}[o];P[d]=c;Q[c]=Q.get(c,0)+1;break
 E=[p if Q[p:=P[e]]==1 else e for e in P]
X,Y=*zip(*E),;print((max(X)-min(X)+1)*(max(Y)-min(Y)+1)-len(E))