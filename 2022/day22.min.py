import re;F=open('i/22').readlines();G=F[:-2];X=max(len(l)for l in G)-1;G=[l[:-1]+' '*X for l in G];x=G[0].index('.');u=1;y=v=0;L=-1;R=-2
for n in eval(re.sub('(\\d+|L|R)','\\1,',F[-1])):
 u,v=*((v,-u)if n==L else(-v,u)if n==R else(u,v)),
 for i in range(n):
  z=1;a,b=x,y
  while z or(c:=G[b][a])<'!':z=0;a,b=(a+u)%X,(b+v)%len(G)
  if c!='#':x,y=a,b
print(y*1000+x*4+1004+[[3,1],[0],[2]][u][v])