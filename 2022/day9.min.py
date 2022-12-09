t=(h:=[0,0])[:];O={'U':'1]+','D':'1]-','L':'0]-','R':'0]+'}
def f(d):
 exec(f'h[{O[d]}=1');dx=h[0]-t[0];dy=h[1]-t[1]
 if dy>1:t[1]+=1;t[0]+=dx
 if dy<-1:t[1]-=1;t[0]+=dx
 if dx>1:t[0]+=1;t[1]+=dy
 if dx<-1:t[0]-=1;t[1]+=dy
 return tuple(t)
print(len(set(f(d)for l in open('i/9').readlines()for d in l[0]*int(l[2:]))))