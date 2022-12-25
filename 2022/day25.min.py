d=0;s=''
for l in open('i/25').readlines():
 x=0
 for c in l[:-1]:x*=5;x+=2-'210-='.index(c)
 d+=x
while d>0:r=d%5;s='012-='[r]+s;d=d//5+(r>2)
print(s)