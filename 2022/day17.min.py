R=[(0,0)];J=open('i/17').read();j=0;M=lambda:max(c[1]for c in R)
for i in range(2022):
 A=i%5*10;s=[eval(','.join('00102030001001112112001020212200010203000001101100'[r:r+2]))for r in range(A,A+10,2)];x=2;y=M()+4;K=lambda m,n:n and all((m+a,n+b)not in R for a,b in s);L=1
 while L:x+=-(x and K(x-1,y))if J[j%len(J)]<'>'else x<[3,4,4,6,5][i%5]and K(x+1,y);j+=1;L=K(x,y-1);y-=L
 R+=[(x+a,y+b)for a,b in s]
print(M())