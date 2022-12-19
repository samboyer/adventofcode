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
import re;from collections import deque;print(sum(Q(*eval(re.sub('[^0-9]+',',',l)[1:]))for l in open('i/19').readlines()))