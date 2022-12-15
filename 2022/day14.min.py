R=[(x,y)for(a,b),(c,d)in[sorted(p)for w in[[*map(eval,l.split('->'))]for l in open('i/14').readlines()]for p in zip(w,w[1:])]for x in range(a,c+1)for y in range(b,d+1)];M=max(c[1]for c in R);i=0
def f(x,y):Y=y+1;return y<M and(((R.append((x,y))or True if(x+1,Y)in R else f(x+1,Y))if(x-1,Y)in R else f(x-1,Y))if(x,Y)in R else f(x,Y))
while f(500,0):i+=1
print(i)