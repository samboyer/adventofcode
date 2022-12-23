# day 20 - circular array reordering
# answer = 14526

# zip each number with its original location in the array,
# delete/insert each elem in their original order.


I=*map(int,open('i/20').readlines()),;
L=len(I);
R=range(L);
A=[*zip(I,R)];
#newline
for i in R:
  #newline#space
  o=A.index(b:=(x:=I[i],i))
  #newline#space
  if x:
    del A[o];
    A.insert((o + x)%(L-1),b)
#newline
print(
  sum(
    [
      A[(l*1000+A.index((0,I.index(0))))%L][0]
      for l in
      [1,2,3]
    ]
  )
)





#end
exit()


I=*map(int,open('i/20').readlines()),
L=len(I)
R=range(L)
A=[*zip(I,R)]

def debug():
  print([x for (x,i) in A])

# debug()

for i in R:
    original_loc,x,_ = [(j,*A[j])for j in R if A[j][1]==i][0]

    if x == 0: continue

    del A[original_loc]

    new_position = (original_loc + x)%(L-1)
    A.insert(new_position,(x,i))


z=[j for j in R if A[j][0]==0][0]
locs=[(1000+z)%L,(2000+z)%L,(3000+z)%L]
print(z, locs)
print(sum([A[l][0] for l in locs]))



