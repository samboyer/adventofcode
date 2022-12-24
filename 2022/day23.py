# day 23 - elf movement
# answer = 4172


# overall design - store coordinates of each elf

# notes:
# - directions are global; round one is NSWE, 2 is SWEN; 3 is WENS; 4 is ENSW etc
#     [NSWE,SWEN,WENS,ENSW][r%4]



F=open('i/23').readlines();
R=range;
E=[(x,y)for y in R(len(F)) for x in R(len(F[-1])) if F[y][x]=='#']
#newline
for r in R(10):
  #newline#space
  P={};
  Q={}
  #newline#space
  for x,y in E:
    #newline#space#space
    d=(x,y);
    A=*zip([x-1,x,x+1]*3,[y-1]*3+[y]*3+[y+1]*3),
    #newline#space#space
    for o in '1'+['NSWE','SWEN','WENS','ENSW'][r%4]+'0': #o<- 'N','S','W'...
      #newline#space#space#space
      if all(a==4 or A[a] not in E for a in {'N':(0,1,2), 'S':(6,7,8), 'W':(0,3,6), 'E':(2,5,8),'0':(),'1':R(9)}[o]):
        c={'N':A[1],'S':A[7],'W':A[3],'E':A[5],'0':d,'1':d}[o];
        P[d] = c;
        Q[c]=Q.get(c,0)+1;
        break
  #newline#space
  # part 2
  E=[p if Q[p:=P[e]]==1 else e for e in P]

#newline

X,Y=*zip(*E),; # who knew zip could do this?!?!?!

print((max(X)-min(X)+1)*(max(Y)-min(Y)+1)-len(E))


#end
exit()

def debug():
  minx = min(i for (i,j) in E)
  maxx = max(i for (i,j) in E)
  miny = min(j for (i,j) in E)
  maxy = max(j for (i,j) in E)
  for y in range(miny,maxy+1):
    for x in range(minx,maxx+1):
      print('#' if (x,y) in E else '.', end='')
    print()
  print()




F=open('i/23').readlines()
R=range
E=[(x,y)for y in R(len(F)) for x in R(len(F[-1])) if F[y][x] == '#']

# debug()



# adj=[
#   (-1,-1),#NW
#   (0,-1),  #N
#   (1,-1),#NE
#   (-1,0),  #W
#   (1,0),  #E
#   (-1,1),#SW
#   (0,1),  #S
#   (1,1),#SE
# ]
# @@@ compress this??


for r in range(10):
  print(r)
  # part 1: work out desired destination of each elf, accumulate proposed positions
  proposed = {} #keyed on elf current coordinate, val is proposed coordinate
  # proposed_counts={} #keyed on coordinate, val is num of elves that want to go there
  # @@@ should be able to do proposed.values.count() instead, but unsure which is shorter

  for x,y in E:
    # order = [NSWE,SWEN,WENS,ENSW][r%4]
    order = '1'+['NSWE','SWEN','WENS','ENSW'][r%4]+'0'
    # print(order)

    adj=[
      (x-1,y-1),#NW
      (x,y-1),  #N
      (x+1,y-1),#NE
      (x-1,y),  #W
      (x+1,y),  #E
      (x-1,y+1),#SW
      (x,y+1),  #S
      (x+1,y+1),#SE
      ]
    # if all(c not in E for c in adj):
    #   #don't move if no adjacent elves
    #   print(f'({x},{y}) staying still')
    #   proposed[(x,y)] = (x,y)
    #   continue

    dirs={'N':(0,1,2), 'S':(5,6,7), 'W':(0,3,5), 'E':(2,4,7),'0':(),'1':(*R(8),)}
    moves={'N':adj[1],'S':adj[6],'W':adj[3],'E':adj[4],'0':(x,y),'1':(x,y)}
    # print(adj)
    # print(order)
    # print(dirs[order[0]])
    # print([adj[a] for a in dirs[order[0]]])
    # print(all(adj[a] not in E for a in dirs[order[0]]))
    for o in order: #o<- 'N','S','W'...
      if all(adj[a] not in E for a in dirs[o]):
        proposed[(x,y)] = moves[o]
        # print(f'({x},{y}) moving in dir {o}')
        break

  # part 2 - make moves if possible
  E=[]
  # print(proposed)
  for e,p in proposed.items():
    E+=[p if [*proposed.values()].count(p)==1 else e]
  # print(E)

  # debug()
  # input()


# debug()

# answer is (xmax-xmin)*(ymax-ymin)-len(elves)

minx = min(i for (i,j) in E)
maxx = max(i for (i,j) in E)+1
miny = min(j for (i,j) in E)
maxy = max(j for (i,j) in E)+1
print((maxx-minx)*(maxy-miny)-len(E))