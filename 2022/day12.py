# day 12 - hill climbing
# answer = 330

# (do a BFS of the path space)

def h(x,y,l):#newline#space
  if f[y][x]==69:
    print(l)
    #newline#space
  c=max(f[y][x],96); #char at this position (replacing S with a-1 so it can do initial move)
  # print(x,y,l,chr(f[y][x]))
  #only consider this coordinate if
  # - it's inside the grid
  # - it hasn't been seen already
  # - and its height value is <=f[y][x]+1 and not S or E
  #   - OR it's >='y'
  # if these tests pass, add this coordinate to the visited and state queue
  [
    V.append((a,b))or#space
    Q.append((a,b,l+1))
    for a,b in[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    if 0<=a<X and 0<=b<Y and(a,b)not in V and(96<f[b][a]<=c+1 or c>120)
  ]

#newline

f=open('i/12','rb').readlines();
X=len(f[0])-1;
Y=len(f);

# Q = queue of search states. initial state is the position of 'S', and path length 0.
Q=[(x,y,0)for y in range(Y)for x in range(X)if f[y][x]==83];
# V= set of visited tiles (don't visit again)
V=[];
# print(X,Y)
[h(*q)for q in Q] #self-populating list comprehesion:)


# ascii table: 'a'=0x97, 0x61. 'z'=0d122, 0x7A
# 'E'=69