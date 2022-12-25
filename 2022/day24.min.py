F=[l[1:-2]for l in open('i/24').readlines()[1:-1]];R=range;X=len(F[0]);Y=len(F);B=[(i,j,F[j][i])for j in R(Y)for i in R(X)if F[j][i]in '^>v<'];S=[B:=[((i+{'>':1,'<':-1}.get(d,0))%X,(j+{'v':1,'^':-1}.get(d,0))%Y,d)for(i,j,d)in B]for i in R(X*Y)];W=[{b[:2]for b in s}for s in S];Q=[(0,-1,0)];V=set();g=(X-1,Y)
def z(t):Q.append(t);V.add(t)
def h(x,y,t):
 if(x,y)==g:print(t);exit()
 [z((*c,t+1))for c in[(x-1,y),(x+1,y),(x,y+1),(x,y),(x,y-1)]if(0<=c[0]<X and 0<=c[1]<Yor c in(g,(0,-1)))and c not in W[t]and(*c,t+1)not in V]
[h(*q)for q in Q]