# day 22 - map navigation
# answer = 26558

import re;
F=open('i/22').readlines();
G=F[:-2];
X=max(len(l) for l in G)-1; #omit newline
G=[l[:-1]+' '*X for l in G]; #pad every line to prevent lookup errors
x=G[0].index('.');
u=1;
y=v=0;
L=-1;R=-2

#newline


for n in eval(
    re.sub('(\\d+|L|R)','\\1,',F[-1])
  ):
  #newline#space
  u,v=*((v,-u) if n==L else (-v,u) if n==R else (u,v)),
  #newline#space
  for i in range(n): #won't run if n is L/R
    #newline#space#space
    # move in dir (u,v), wrap around if necessary
    z=1;
    a,b=x,y
    #newline#space#space
    # while z or (c:=G[b][a])==' ':
    while z or (c:=G[b][a])<'!':
      z=0; # do it at least once
      a,b=(a+u)%X,(b+v)%len(G)
    #newline#space#space
    if c!='#':
        x,y=a,b

#newline

# lut=[(1,0),(0,1),(-1,0),(0,-1)]; # score is the index of the dir
# print((y+1)*1000 + (x+1)*4 + lut.index((u,v)))

# lut={1:[0],0:{1:1,-1:3},-1:[2]}; # terrifying compression of 2d array
# lut={1:[0],0:[3,1],-1:[2]};      # omg it got worse
# lut=[[3,1],[0],[2]];             # stooooop

print(y*1000+x*4+1004+[[3,1],[0],[2]][u][v])



#end

exit()

# ORIGINAL CODE

F=open('i/22').readlines();
X=max(len(l) for l in F[:-2])-1; #omit newline
Y=len(F)-2; #omit empty line, instructions
print(X,Y)
G=[l[:-1]+' '*X for l in F[:-2]] #pad every line to prevent lookup errors
pos=(F[0].index('.'),0)
d=(1,0)

clockwise = lambda x,y:(-y,x)
anticlockwise = lambda x,y:(y,-x)
# clockwise
# (1,0) (right) -> (0,1) down -> (-1,0) (left) -> (0,-1) (up)
# anticlockwise
# (1,0) -> (0,-1) -> (-1,0) -> (0,1)

import re;

L=-1;R=-2;

for n in eval(
    re.sub('(\\d+|L|R)','\\1,',F[-1][:-1])
  ):
  if n==L:
    print('turning left')
    d=anticlockwise(*d)
  elif n==R:
    print('turning right')
    d=clockwise(*d)
  else:
    print(f'moving {n} places in dir {d}')
    # move by i places
    for i in range(n):
      # move in d, wrap around if necessary
      z=1
      p2=pos
      while z or G[p2[1]][p2[0]] == ' ':
        z=0#do it at least once
        # @@@ don't move if it's a wall ahead
        # (gonna be hard when it's a looparound block) aaand yep it just happened
        # need to factor spaces into p2 calculation (ie one while loop per p2), then only move if landed on is not a #
        p2=((p2[0]+d[0])%X,(p2[1]+d[1])%Y)
      if G[p2[1]][p2[0]] !='#':
          pos=p2
      # print(pos,G[pos[1]][pos[0]])


def password(c,r,dir):
  lut=[(1,0),(0,1),(-1,0),(0,-1)]
  return (r+1)*1000+(c+1)*4+lut.index(dir)

print(password(*pos,d))



"""
ideas:
10R5L5R10L4R5L5
V convert to V
10,R,5,L,...
V   V
f(i) if i in [L,R] else f(i) for i in eval({})
"""
