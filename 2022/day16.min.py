import re;from collections import deque;Q=deque([('AA',30,0,[])]);S={};N={a:(int(b),c)for a,b,*c in[re.findall('[A-Z]{2}|\\d+',l)for l in open('i/16').readlines()]};M=0
while len(Q):l,t,p,o=Q.popleft();T=t-1;M=max(M,p);Q+=[]if(l,p)in S or t<1 else([]if l in o or N[l][0]==0 else[(l,T,p+N[l][0]*T,o+[l],)])+[(a,T,p,o)for a in N[l][1]];S[(l,p)]=1
print(M)