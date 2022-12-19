# day 19 - robot construction
# answer = 988

def Q(i,a,b,c,d,e,f):
  #newline#space
  # state = (
  # 0. num robots of each type (ore,clay,obsidian,geode)
  # 1. mins remaining
  # 2. amount of each resource (ore,clay,obsidian,geodes))
  Q=deque([
    ([0]*4,24,[0]*4)
  ]);
  z=0;

  S={}
  #newline#space
  while len(Q):
    #newline#space#space
    X,t,r = Q.pop(); #bots, mins remaining, resources
    # (b_ore,b_clay,b_obs,b_geo)=X;
    # (r_ore,r_clay,r_obs,r_geo)=r;
    (u,v,w,g)=X;
    (U,V,W,G)=r;
    T=t-1;
    # n,N,j,J=[u+U+1,v+V,w+W,g+G]; #implicit 1 ore robot to make shorter initial state
    n=u+U+1;N=v+V;j=w+W;J=g+G;
    z=max(z,J)
    #newline#space#space
    if T<1 or(*X,t,*r) in S:continue
    #newline#space#space
    S[(*X,t,*r)]=1;
    #newline#space#space
    if U>=e and W>=f: #make geode robot
      Q+=[([u,v,w,g+1],T,[n-e,N,j-f,J])]
    #newline#space#space
    else:
      #newline#space#space#space
      if U>=a: #make ore robot
        Q+=[([u+1,v,w,g],T,[n-a,N,j,J])]
      #newline#space#space#space
      if U>=b: #make clay robot
        Q+=[([u,v+1,w,g],T,[n-b,N,j,J])]
      #newline#space#space#space
      if U>=c and V>=d: #make obsidian robot
        Q+=[([u,v,w+1,g],T,[n-c,N-d,j,J])]
      #newline#space#space#space
      Q+=[(X,T,[n,N,j,J])] #don't make anything
  #newline#space
  return i*z
#newline

import re;from collections import deque;

print(
  sum(
    # quality(*eval(','.join(re.findall('\\d+',l))))
    Q(
      *eval( #eval list string into int list,expand into 7 args, call q
      re.sub('[^0-9]+',',',l)[1:] #replace blueprint string with list of nums
      )
    )
    for l in open('i/19').readlines()
  )
)



#end
exit()

# ORIGINAL CODE

from collections import deque;

# a BFS over the state space? in this economy??
# (this is the 3rd time now)

# Blueprints: ore, clay, obsidian, geode
# always 7 nums:
# 0/i. blueprint num
# 1/a. ore robot ore cost
# 2/b. clay robot ore cost
# 3/c. obsidian robot ore cost
# 4/d. obsidian robot clay cost
# 5/e. geode robot ore cost
# 6/f. geode robot obsidian cost

def quality(i,a,b,c,d,e,f):
  print(i,a,b,c,d,e,f)

  # queue of states, starting at initial state.
  # state = (
  # 0. num robots of each type (ore,clay,obsidian,geode)
  # 1. mins remaining
  # 2. amount of each resource (ore,clay,obsidian,geodes))
  Q=deque([
    ([1,0,0,0],24,[0]*4)
  ]);
  z=0

  S={}

  debug_ctr=0

  while len(Q)>0:
    debug_ctr+=1
    if debug_ctr==100000:
      # print(Q[-1])
      # print(len(Q))
      debug_ctr=0

    X,t,r = Q.pop(); #bots, mins remaining, resources
    (b_ore,b_clay,b_obs,b_geo)=X
    (r_ore,r_clay,r_obs,r_geo)=r;
    if (*X,t,*r) in S:continue
    S[(*X,t,*r)]=1
    T=t-1;
    # R=*map(sum,zip(x,r)),; # each bot mines one of its respective resource (add b to r)
    R=[r_ore+b_ore,r_clay+b_clay,r_obs+b_obs,r_geo+b_geo]

    z=max(z,R[3])

    # don't push new states if they don't count
    if T<1: continue
    # consider making one of each bot with existing resources.

    # OPTIMISATION: if you had the resources you'd always make a geode robot
    # rather than doing anything else.
    if r_ore>=e and r_obs>=f: #make geode robot
      P=R[:];P[0]-=e;P[2]-=f;
      Q+=[((b_ore,b_clay,b_obs,b_geo+1),T,P)]
    else:
      if r_ore>=a: #make ore robot
        P=R[:];P[0]-=a
        Q+=[((b_ore+1,b_clay,b_obs,b_geo),T,P)]

      if r_ore>=b: #make clay robot
        P=R[:];P[0]-=b
        Q+=[((b_ore,b_clay+1,b_obs,b_geo),T,P)]

      if r_ore>=c and r_clay>=d: #make obsidian robot
        P=R[:];P[0]-=c;P[1]-=d;
        Q+=[((b_ore,b_clay,b_obs+1,b_geo),T,P)]

      # if r_ore<max(a,b,c,e):
      Q+=[((b_ore,b_clay,b_obs,b_geo),T,R)] #don't make anything

    # # consider making one of each bot with existing resources
    # if r[0]>a: #make ore robot
    #   B=x[:];B[0]+=1
    #   P=R[:];P[0]-=a
    #   Q+=[(B,T,P)]

    # if r[0]>b: #make clay robot
    #   B=x[:];B[1]+=1
    #   P=R[:];P[0]-=b
    #   Q+=[(B,T,P)]

    # if r[0]>c and r[1]>d: #make obsidian robot
    #   B=x[:];B[2]+=1
    #   P=R[:];P[0]-=c;P[1]-=d;
    #   Q+=[(B,T,P)]

    # if r[0]>e and r[2]>f: #make geode robot
    #   B=x[:];B[3]+=1
    #   P=R[:];P[0]-=e;P[2]-=f;
    #   Q+=[(B,T,P)]
    # # don't make anything
    # Q+=[(x,T,R)]


  # @@@ this might be shorter?
  # max(h(*q)for q in Q) #self-populating list comprehesion:)

  print(i,z)
  return i*z

import re;

print(
  sum(
    # quality(*eval(','.join(re.findall('\\d+',l))))
    quality(
      *eval( #eval list string into int list,expand into 7 args, call q
      re.sub('[^0-9]+',',',l)[1:] #replace blueprint string with list of nums
      )
    )
    for l in open('i/19.example').readlines()
  )
)


print()

print(
  [
    eval( #eval list string into int list,expand into 7 args, call q
      re.sub('[^0-9]+',',',l)[1:] #replace blueprint string with list of nums
    )
    for l in open('i/19.example').readlines()
  ]
)
