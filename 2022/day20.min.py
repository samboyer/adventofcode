I=*map(int,open('i/20').readlines()),;L=len(I);R=range(L);A=[*zip(I,R)];
for i in R:
 o=A.index(b:=(x:=I[i],i))
 if x:del A[o];A.insert((o+x)%(L-1),b)
print(sum([A[(l*1000+A.index((0,I.index(0))))%L][0]for l in[1,2,3]]))