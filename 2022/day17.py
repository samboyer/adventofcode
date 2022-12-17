# day 17 - tetris simluator
# answer = 3081
# this one started at about 540 chars, so golfing it down to 420 chars was pretty fun!

# assumptions/design choices:
# - shapes are anchored at their bottom-left point
# - coordinates are expressed (x,y)


# list of coordinate for squares filled in
# (y=0 implicitly included, but 0,0 explicitly added to avoid max() failing on an empty list
R = [(0,0)];

# def print_rocks():
#   max_y = max(c[1] for c in R)
#   for y in range(max_y+1,-1,-1):
#     for x in range(7):
#       print('#' if (x,y) in R else '=' if y==0 else'.',end='')
#     print()

# list of jet directions
J=open('i/17').read();
j=0;
M=lambda:max(c[1] for c in R)

#newline

for i in range(2022):
  #newline#space

  # derive a list of coordiates for the i'th shape
  # (this took a *LOT* of golfing :P)

  # s=[
  #   [(0,0),(1,0),(2,0),(3,0)], # --
  #   [(1,0),(0,1),(1,1),(2,1),(1,2)], # +
  #   [(0,0),(1,0),(2,0),(2,1),(2,2)], # _|
  #   [(0,0),(0,1),(0,2),(0,3)], # |
  #   [(0,0),(0,1),(1,0),(1,1)] # []
  # ][i%5];

  # z=i%5;
  # s=list(zip(
  #   map(int,['0123','10121','01222','0000','0011'][z]),
  #   map(int,['0000','01112','00012','0123','0101'][z])
  # ));
  A=i%5*10;
  # s=['00102030001001112112001020212200010203000001101100'[r:r+2]for r in range(A,A+10,2)];
  s=[eval(','.join('00102030001001112112001020212200010203000001101100'[r:r+2]))for r in range(A,A+10,2)];


  x = 2;
  y = M() + 4;
  # I=lambda m,n:any((m+a,n+b)in R for a,b in s)or n==0; #returns True if shape s is intersecting with any previous shapes, or the ground at y=0

  K=lambda m,n:n and all((m+a,n+b)not in R for a,b in s); #returns False if shape s is intersecting with any previous shapes, or the ground at y=0

  L=1 #loop condition

  #newline#space
  while L:
    # print(i,x,y, intersects(s,x,y-1), J[j%len(J)])

    # move the shape according to jet stream, clamp between 0..7
    # if J[j%len(J)] == '<':
    #   x-=0 if x<1 or I(x-1,y) else 1
    #   #newline#space#space
    # else:
    #   x+=0 if x>6-[4,3,3,1,2][i%5] or I(x+1,y) else 1
    # #newline#space#space

    # x-=0 if J[j%len(J)] == '>'or x<1 or I(x-1,y) else 1; #left
    # x+=0 if J[j%len(J)] == '<'or x>6-[4,3,3,1,2][i%5] or I(x+1,y) else 1; #right

    # x += (0 if x<1 or I(x-1,y) else -1)if J[j%len(J)] == '<'else 0 if x>6-[4,3,3,1,2][i%5] or I(x+1,y) else 1;
    # x += (0 if x<1 or I(x-1,y) else -1)if J[j%len(J)] == '<'else not(x>[2,3,3,5,4][i%5] or I(x+1,y));
    # x += -(not(x<1 or I(x-1,y)))if J[j%len(J)] == '<'else not(x>[2,3,3,5,4][i%5] or I(x+1,y));
    x += -(x and K(x-1,y)) if J[j%len(J)]<'>'else x<[3,4,4,6,5][i%5] and K(x+1,y);

    j+=1;

    # break loop if it's touching the ground
    L=K(x,y-1);
    # only allow downwards move if it doesn't intersect (I true=1, 1-1=0, I false=0, 1-0=1)
    y-=L
  #newline#space
  # solidify this shape by adding all elements to the rock list
  R+=[(x+a,y+b) for a,b in s]

  # print_rocks();
  # input()
#newline
print(M())

# def I(x,y):return any(((x+a,y+b)in R)for a,b in s)


#end
exit()
# ORIGINAL CODE
shapes = [
  [(0,0),(1,0),(2,0),(3,0)], # --
  [(1,0),(0,1),(1,1), (2,1), (1,2)], # +
  [(0,0),(1,0),(2,0),(2,1),(2,2)], # _|
  [(0,0),(0,1),(0,2),(0,3)], # |
  [(0,0),(0,1),(1,0),(1,1)], # []
]
widths = [4,3,3,1,2]

# list of coordinate for squares filled in
# (ground is filled in already)
rocks = [(i,0)for i in range(7)]

def print_rocks():
  max_y = max(c[1] for c in rocks)
  for y in range(max_y+1,-1,-1):
    for x in range(7):
      print('#' if (x,y) in rocks else '.',end='')
    print()



# list of jet coordinates
J=open('i/17').read()
j=0

def intersects(s,x,y):
  # Does shape s at x,y intersect with any rock pieces?
  return any(((x+a,y+b) in rocks) for a,b in s)

def solidify(s,x,y):
  [rocks.append((x+a,y+b)) for a,b in s]

for i in range(2022):
  s=shapes[i%5]
  w=widths[i%5]
  max_y = max(c[1] for c in rocks)
  x=2
  y=max_y+4

  while 1:
    # print(i,x,y, intersects(s,x,y-1), J[j%len(J)])
    # move the shape according to jet stream, clamp between 0..7
    if J[j%len(J)] == '<' :
      x-=0 if x<1 or intersects(s,x-1,y) else 1
    else:
      x+=0 if x>6-w or intersects(s,x+1,y) else 1
    j+=1
    if intersects(s,x,y-1): break
    # allow a push while touching the ground, but break before trying to move down again.
    y-=1
  # solidify this shape by adding all elements to the rock list
  solidify(s,x,y)
  # print_rocks()
  # input()

max_y = max(c[1] for c in rocks)
print(max_y)
