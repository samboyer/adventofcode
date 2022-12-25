# day 25 -
# answer= '122-0==-=211==-2-200'

# d=sum(
#   (2-'210-='.index(l[-2-i])) * 5**i#space
#   for l in open('i/25').readlines()
#   for i in range(len(l)-1)
# );

d=0;
s=''

#newline
for l in open('i/25').readlines():
  #newline#space
  x=0
  #newline#space
  for c in l[:-1]:
    x*=5;x+=2-'210-='.index(c)
  #newline#space
  d+=x
#newline


while d>0:
  r=d%5;
  s='012-='[r]+s;
  d=d//5+(r>2)
#newline

print(s)



#end
exit()
#ORIGINAL CODE
LUT={'2':2,'1':1,'0':0,'-':-1,'=':-2}

d=sum(
  LUT[l[-2-i]]*5**i
  for l in open('i/25').readlines()
  for i in range(len(l)-1)
)
# print(d)

s=''
while d>0:
  r=d%5
  if r<3:
    s=str(r)+s
    d//=5
  else:
    s= ('-','=')[r<4]+s
    d//=5
    d+=1

print(s)
