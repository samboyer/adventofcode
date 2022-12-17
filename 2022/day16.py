# day 16 - flow maximiser
# (state space exploration)
# answer = 1940

import re;
from collections import deque;


# queue of states, starting at initial state
# state = (current location,mins remaining, working pressure, valves opened)
Q=deque([('AA',30,0,[])]);

# list of 'visited states', to avoid backward steps
# tuples are now (current location, working pressure),
# so we can actually compare states properly.
# NOTE the traversal MUST be done as a BFS instead of DFS
# because we skip if the position has been seen before.
# )it's a dict for necessary performance reasons)
S={};
# network of valves & tunnels
N={
  a:(int(b),c)
  for a,b,*c in [
    re.findall('[A-Z]{2}|\\d+',l)
    for l in open('i/16').readlines()
  ]
};
# print(N)

# max working pressure we've seen
M=0

#newline
while len(Q):
  #(current location,mins remaining, working pressure, valves opened)
  l,t,p,o=Q.popleft();

  T=t-1; #new time after doing action at this valve
  M=max(M,p);

  Q+=[] if (l,p) in S or t<1 else (
    # consdier opening this valve (if it's not been opened already and has >0 flow)
    []
    if l in o or N[l][0]==0#space
    else [
      (
        l, #don't move
        T, #new time
        p+N[l][0]*T, #flow * remaining time
        o+[l], #open this valve
      )
    ]
  )+[ # consider moving
    (
      a, #move to adjacent
      T,
      p, #we didn't open anything
      o #didn't open anything
    )
    for a in N[l][1] #for each adjacent valve to this valve
  ];
  S[(l,p)]=1
#newline
print(M)



#end
exit()
# ORIGINAL CODE

import re;
from collections import deque;
# queue of states, starting at initial state
# state = (current location,mins remaining, working pressure, valves opened, valves visited)
# places you've been to
Q=deque([('AA',30,0,[],[])]);

# list of 'visited states', to avoid backward steps
# tuples are now (current location, working pressure),
# so we can actually compare states properly.
# NOTE the traversal MUST be done as a BFS instead of DFS
# because we skip if the position has been seen before.
# )it's a dict for necessary performance reasons)
S={};

# network of valves & tunnels
N={
  x[0]:(int(x[1]),x[2:])
  for x in [
    re.findall('[A-Z]{2}|\\d+',l)
    for l in open('i/16').readlines()
  ]
};
# print(N)

# max working pressure we've seen
M=0

# debug_iters=0
# import time
# dur=0

while len(Q)>0:
  # print(len(Q))
  # t0=time.time()

  #(current location,mins remaining, working pressure, valves opened, valves visited)
  # l,t,p,o,v=Q[0];
  # Q=Q[1:];
  l,t,p,o,v=Q.popleft();

  T=t-1; #new time after doing action at this valve
  M=max(M,p);

  if(l,p)in S:continue
  S[(l,p)]=1

  # consdier opening this valve (if it's not been opened already and has >0 flow)
  Q+=[] if t<1 or l in o or N[l][0]==0 else [(
    l, #don't move
    T, #new time
    p+N[l][0]*T, #flow * remaining time
    o+[l], #open this valve
    v+[l], #this valve has been visited
  )];
  # consider moving
  Q+=[
    (
      a, #move to adjacent
      T,
      p, #we didn't open anything
      o, #didn't open anything
      v+[l], #this valve has been visited
    )
    for a in N[l][1] #for each adjacent valve to this valve
    if t>0 # if this valve hasn't been visited yet
  ];

  # t1=time.time()
  # dur+=t1-t0
  # debug_iters+=1
  # if debug_iters==1000:
  #   print(f"mins remaining={Q[0][1]}, iter time={dur/1000*1000}ms")
  #   debug_iters=0
  #   dur=0

print(M)
