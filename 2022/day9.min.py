t=(h:=[0,0])[:];O={'U':'1]+','D':'1]-','L':'0]-','R':'0]+'}
def f(d):
 exec(f'h[{O[d]}=1');x=h[0]-t[0];y=h[1]-t[1]
 if y>1:t[1]+=1;t[0]+=x
 if y<-1:t[1]-=1;t[0]+=x
 if x>1:t[0]+=1;t[1]+=y
 if x<-1:t[0]-=1;t[1]+=y
 return tuple(t)
print(len(set(f(d)for l in open('i/9').readlines()for d in l[0]*int(l[2:]))))