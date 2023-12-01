from collections import deque
import re
_r=range
_p=print
_u=lambda f:open(f).read()
_v=lambda f:open(f).readlines()
_p(max(sum(map(int,e.split('\n')))for e in _u('i/1')[:-1].split('\n\n')))
_p(sum('BXCYAZAXBYCZCXAYBZ'.index(l[::2])//2+1 for l in _v('i/2')))
_p(sum(26+(c&31)-(c&32 and 26)for c in[[l for l in s[:len(s)//2]if l in s[len(s)//2:]][0]for s in open('i/3','rb').readlines()]))
_p(len([l for l in _v('i/4')for a,b,c,d in[map(int,re.split(',|-',l))]if(a<=c and b>=d)or(c<=a and d>=b)]))
f=_v('i/5');a=f.index('\n');s=[' ']+[[l[i]for l in f[:a]if l[i]!=' ']for i in _r(1,len(f[0]),4)]
for n,x,y in[[int(i)for i in l.split()if i.isdigit()]for l in f[a+1:]]:s[y]=s[x][:n][::-1]+s[y];del s[x][:n]
_p(''.join(l[0]for l in s))
s=_u('i/6');_p([len(set(s[i:i+4]))for i in _r(len(s))].index(4)+4)
def f(s,c,a=0):
 if c=='cd':
  if a[0]<'/':b[0]+=x if(x:=b.pop())<=100000 else 0;b[-1]+=x
  else:b.append(0)
 if s.isdigit():b[-1]+=int(s)
b=[0];[f(*l.split(' '))for l in _v('i/7')];[f('','cd','.')for _ in b];_p(b[0])
g=open('i/8','rb').readlines();n=_r(len(g));t=[[r[i]for r in g]for i in n];_p(sum([any(all(x<g[j][i]for x in s)for s in[g[j][:i],g[j][i+1:],t[i][:j],t[i][j+1:]])for i in n for j in n]))
t=(h:=[0,0])[:];O={'U':'1]+','D':'1]-','L':'0]-','R':'0]+'}
def f(d):
 exec(f'h[{O[d]}=1');x=h[0]-t[0];y=h[1]-t[1]
 if y>1:t[1]+=1;t[0]+=x
 if y<-1:t[1]-=1;t[0]+=x
 if x>1:t[0]+=1;t[1]+=y
 if x<-1:t[0]-=1;t[1]+=y
 return tuple(t)
_p(len(set(f(d)for l in _v('i/9')for d in l[0]*int(l[2:]))))
def f(i):global X;X+=i;return[X-i,X-i]
X=1;_p(sum([i*x for i,x in enumerate(sum((f(int(l[4:]))if 'a' in l else[X] for l in _v('i/10')),[0]))][20::40]))
def k(m):
 for old in m[0]:n=eval(m[1])//3;d=int(m[4]if n%m[2]else m[3]);M[d][0]+=[n];m[5]+=1
 m[0]=[]
M=[[[int(l)for l in t[1][18:].split(',')],t[2][19:],int(t[3][21:]),t[4][29:],t[5][30:],0]for t in[m.split('\n')for m in _u('i/11').split('\n\n')]];[k(m)for i in[0]*20 for m in M];s=sorted(m[5]for m in M);_p(s[-1]*s[-2])
def h(x,y,l):
 if f[y][x]==69:_p(l)
 c=max(f[y][x],96);[V.append((a,b))or Q.append((a,b,l+1))for a,b in[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]if 0<=a<X and 0<=b<Y and(a,b)not in V and(96<f[b][a]<=c+1 or c>120)]
f=open('i/12','rb').readlines();X=len(f[0])-1;Y=len(f);Q=[(x,y,0)for y in _r(Y)for x in _r(X)if f[y][x]==83];V=[];[h(*q)for q in Q]
def L(x):return[x]if type(x)==int else x
def e(l,r):
 if[]in[l,r]:return len(l)-len(r)
 a=l[0];b=r[0];t=e(l[1:],r[1:]);return a-b or t if type(a)==type(b)==int else e(L(a),L(b))or t
f=[eval(l)for l in _v('i/13')if l!='\n'];_p(sum(i//2+1for i in _r(0,len(f),2)if e(f[i],f[i+1])<1))
R=[(x,y)for(a,b),(c,d)in[sorted(p)for w in[[*map(eval,l.split('->'))]for l in _v('i/14')]for p in zip(w,w[1:])]for x in _r(a,c+1)for y in _r(b,d+1)];M=max(c[1]for c in R);i=0
def f(x,y):Y=y+1;return y<M and(((R.append((x,y))or True if(x+1,Y)in R else f(x+1,Y))if(x-1,Y)in R else f(x-1,Y))if(x,Y)in R else f(x,Y))
while f(500,0):i+=1
_p(i)
_p(len(set.union(*[set(_r(a-(x:=abs(a-c)+abs(b-d)-abs(b-2000000)),a+x))for a,b,c,d in[map(int,re.findall('-?\d+',l))for l in _v('i/15')]])))
Q=deque([('AA',30,0,[])]);S={};N={a:(int(b),c)for a,b,*c in[re.findall('[A-Z]{2}|\\d+',l)for l in _v('i/16')]};M=0
while len(Q):l,t,p,o=Q.popleft();T=t-1;M=max(M,p);Q+=[]if(l,p)in S or t<1 else([]if l in o or N[l][0]==0 else[(l,T,p+N[l][0]*T,o+[l],)])+[(a,T,p,o)for a in N[l][1]];S[(l,p)]=1
_p(M)
R=[(0,0)];J=_u('i/17');j=0;M=lambda:max(c[1]for c in R)
for i in _r(2022):
 A=i%5*10;s=[eval(','.join('00102030001001112112001020212200010203000001101100'[r:r+2]))for r in _r(A,A+10,2)];x=2;y=M()+4;K=lambda m,n:n and all((m+a,n+b)not in R for a,b in s);L=1
 while L:x+=-(x and K(x-1,y))if J[j%len(J)]<'>'else x<[3,4,4,6,5][i%5]and K(x+1,y);j+=1;L=K(x,y-1);y-=L
 R+=[(x+a,y+b)for a,b in s]
_p(M())
def f(a,d,*c):e=list(c);e[a]+=d;return(c in G)and(*e,)not in G
G=*map(eval,_v('i/18')),;R=_r(max(sum(G,()))+1);_p(sum(f(a,d,x,y,z)for a in(0,1,2)for d in(-1,+1)for x in R for y in R for z in R))
def Q(i,a,b,c,d,e,f):
 Q=deque([([0]*4,24,[0]*4)]);z=0;S={}
 while len(Q):
  X,t,r=Q.pop();(u,v,w,g)=X;(U,V,W,G)=r;T=t-1;n=u+U+1;N=v+V;j=w+W;J=g+G;z=max(z,J)
  if T<1 or(*X,t,*r)in S:continue
  S[(*X,t,*r)]=1;
  if U>=e and W>=f:Q+=[([u,v,w,g+1],T,[n-e,N,j-f,J])]
  else:
   if U>=a:Q+=[([u+1,v,w,g],T,[n-a,N,j,J])]
   if U>=b:Q+=[([u,v+1,w,g],T,[n-b,N,j,J])]
   if U>=c and V>=d:Q+=[([u,v,w+1,g],T,[n-c,N-d,j,J])]
   Q+=[(X,T,[n,N,j,J])]
 return i*z
_p(sum(Q(*eval(re.sub('[^0-9]+',',',l)[1:]))for l in _v('i/19')))
I=*map(int,_v('i/20')),;L=len(I);R=_r(L);A=[*zip(I,R)];
for i in R:
 o=A.index(b:=(x:=I[i],i))
 if x:del A[o];A.insert((o+x)%(L-1),b)
_p(sum([A[(l*1000+A.index((0,I.index(0))))%L][0]for l in[1,2,3]]))
exec(re.sub('([a-z]+)','\\1()',_u('i/21')).replace('():','=lambda:'));_p(root())
F=_v('i/22');G=F[:-2];X=max(len(l)for l in G)-1;G=[l[:-1]+' '*X for l in G];x=G[0].index('.');u=1;y=v=0;L=-1;R=-2
for n in eval(re.sub('(\\d+|L|R)','\\1,',F[-1])):
 u,v=*((v,-u)if n==L else(-v,u)if n==R else(u,v)),
 for i in _r(n):
  z=1;a,b=x,y
  while z or(c:=G[b][a])<'!':z=0;a,b=(a+u)%X,(b+v)%len(G)
  if c!='#':x,y=a,b
_p(y*1000+x*4+1004+[[3,1],[0],[2]][u][v])
F=_v('i/23');R=_r;E=[(x,y)for y in R(len(F))for x in R(len(F[-1]))if F[y][x]=='#']
for r in R(10):
 P={};Q={}
 for x,y in E:
  d=(x,y);A=*zip([x-1,x,x+1]*3,[y-1]*3+[y]*3+[y+1]*3),
  for o in '1'+['NSWE','SWEN','WENS','ENSW'][r%4]+'0':
   if all(a==4 or A[a]not in E for a in{'N':(0,1,2),'S':(6,7,8),'W':(0,3,6),'E':(2,5,8),'0':(),'1':R(9)}[o]):c={'N':A[1],'S':A[7],'W':A[3],'E':A[5],'0':d,'1':d}[o];P[d]=c;Q[c]=Q.get(c,0)+1;break
 E=[p if Q[p:=P[e]]==1 else e for e in P]
X,Y=*zip(*E),;_p((max(X)-min(X)+1)*(max(Y)-min(Y)+1)-len(E))
F=[l[1:-2]for l in _v('i/24')[1:-1]];R=_r;X=len(F[0]);Y=len(F);B=[(i,j,F[j][i])for j in R(Y)for i in R(X)if F[j][i]in '^>v<'];S=[B:=[((i+{'>':1,'<':-1}.get(d,0))%X,(j+{'v':1,'^':-1}.get(d,0))%Y,d)for(i,j,d)in B]for i in R(X*Y)];W=[{b[:2]for b in s}for s in S];Q=[(0,-1,0)];V=set();g=(X-1,Y)
def z(t):Q.append(t);V.add(t)
def h(x,y,t):
 if(x,y)==g:_p(t);exit()
 [z((*c,t+1))for c in[(x-1,y),(x+1,y),(x,y+1),(x,y),(x,y-1)]if(0<=c[0]<X and 0<=c[1]<Y or c in(g,(0,-1)))and c not in W[t]and(*c,t+1)not in V]
[h(*q)for q in Q]
d=0;s=''
for l in _v('i/25'):
 x=0
 for c in l[:-1]:x*=5;x+=2-'210-='.index(c)
 d+=x
while d>0:r=d%5;s='012-='[r]+s;d=d//5+(r>2)
_p(s)
