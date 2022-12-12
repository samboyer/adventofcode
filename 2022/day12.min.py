def h(x,y,l):
 if f[y][x]==69:print(l)
 c=max(f[y][x],96);[V.append((a,b))or Q.append((a,b,l+1))for a,b in[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]if 0<=a<X and 0<=b<Y and(a,b)not in V and(96<f[b][a]<=c+1 or c>120)]
f=open('i/12','rb').readlines();X=len(f[0])-1;Y=len(f);Q=[(x,y,0)for y in range(Y)for x in range(X)if f[y][x]==83];V=[];[h(*q)for q in Q]