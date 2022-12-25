# day 24 - blizzard traversal
# answer = 279

F=[l[1:-2] for l in open('i/24').readlines()[1:-1]];
R=range;
X=len(F[0]);
Y=len(F);

B=[
  (i,j,F[j][i])
  for j in R(Y) for i in R(X)
  if F[j][i] in '^>v<'
];
#blizzard states at time t
S=[
  #advance B, put a copy in the array, set B for the next iteration
  B:=[
    (
      (i+{'>':1,'<':-1}.get(d,0))%X,
      (j+{'v':1,'^':-1}.get(d,0))%Y,
      d
    )
    for (i,j,d) in B
  ]
  for i in R(X*Y)
];
W = [
  {
    b[:2]
    for b in s
  }
  for s in S
];

# Q=queue of search states, startint with initial state.
# state=(x,y,time/num steps,path)
Q=[(0,-1,0)];
# set of 'visited states' (same items as V, but needed for faster lookups.)
V=set();
# @@@ is there a datatype i can use that allows resizing during iteration?
g=(X-1,Y)
# n=0
#newline
def z(t):
  Q.append(t);
  V.add(t)

#newline

def h(x,y,t):

  #newline#space

  if (x,y)==g: #goal coordinate
    print(t);
    exit()
  #newline#space

  [
    z((*c,t+1))
    for c in [(x-1,y),(x+1,y),(x,y+1),(x,y),(x,y-1)]
    if (
      0<=c[0]<X and 0<=c[1]<Y#space
      or c in(g,(0,-1))
    )
    #disallow stopping on a blizzard tile
    and c not in W[t]
    # disallow adding duplicates
    and (*c,t+1) not in V
  ]

#newline

[h(*q) for q in Q] #self-populating list comprehension :)

#end
exit()

# idea: cache the first X*Y states of the grid, then just BFS through the
# grid, but use state[i] on step i when checking tile accessibility.
# (d12's BFS is most similar, time to plagiariseee)


# ORIGINAL CODE

F=[l[1:-2] for l in open('i/24').readlines()[1:-1]]
R=range

X=len(F[0])
Y=len(F)


LIMIT=X*Y
print(f'limit={LIMIT}')

# print(p)
# print(goal)

B = [
  (i,j,F[j][i])
  for j in R(Y) for i in R(X)
  if F[j][i] in '^>v<'
]

def debug(B,i=-1,j=-1):
  #i,j = current elf position
  s=''
  for y in R(Y):
    for x in R(X):
      bs = [d for (i,j,d) in B if i==x and j==y]
      if x==i and y==j:
        assert bs==[]
        s+='E'
      elif len(bs)==1:
        s+=bs[0]
      elif len(bs)==0:
        s+='.'
      else:
        s+=str(len(bs))
    s+='\n'
  print(s)

def dbg2(path):
  for i in range(len(path)):
    debug(blizzard_states[i],*path[i])

def advance_blizzards():
  global B
  B = [
    (
      (i+(1 if d=='>' else -1 if d=='<' else 0))%X,
      (j+(1 if d=='v' else -1 if d=='^' else 0))%Y,
      d
    )
    for (i,j,d) in B]
  return B

print('populating states...')
blizzard_states=[advance_blizzards()[:] for i in R(LIMIT)]
blizzard_states_walls = [
  {
    (i,j):1
    for (i,j,d) in s
  }
  for s in blizzard_states
]
print('done')


# Q=queue of search states, startint with initial state.
# state=(x,y,time/num steps,path (for debugging @@@ remove in final code))
Q=[(0,-1,0,[])]
# set of 'visited states'
V=set()


n=0

def h(x,y,t,path):
  global n
  n+=1
  if n==1000:
    print(x,y,t)
    n=0


  if t>=LIMIT:return

  def z(i,j):
    Q.append((i,j,t+1,path+[(i,j)]))
    V.add((i,j,t))

  if x==X-1 and y==Y:
    # print(path)
    # dbg2(path)
    print(t)
    exit()
  [
    z(i,j)
    for i,j,d in [
      #ordered to prioritise down/right movement.
      # (symbol is direction a blizzard CAN'T be moving for this move to be valid.)
      (x,y,''),
      (x,y-1,'v'),
      (x-1,y,'>'),
      (x+1,y,'<'),
      (x,y+1,'^'),
    ]
    if t<LIMIT
    and ((0<=i<X and 0<=j<Y) or (i==X-1 and j==Y) or (i==0 and j==-1))#@@@ that is horrible
    #disallow stopping on a blizzard tile
    # and [1 for a,b,_ in blizzard_states[t] if a==i and b==j]==[]
    and (i,j) not in blizzard_states_walls[t]
    # disallow adding duplicates
    and (i,j,t) not in V

    # VV unnecessary (i think)
    #disallow moving THROUGH a blizzard tile
    # (worked out by checking the direction of the )
    # and [1 for a,b,e in blizzard_states[t] if a==i and b==j and d==e]==[]
  ]


# BFS (bad bc it loops over degenerate paths, & combinatorial explosion)
# @@@ maybe I can fix the combinatorial explostion by checking (x,y,d) not in Q???
[h(*q) for q in Q]

# DFS (bad bc it returns suboptimal solutions (e.g. 1599))
# while len(Q):
#   # q=Q[0]
#   # Q=Q[1:]
#   q=Q.pop()
#   h(*q)

print('no solutions:(')