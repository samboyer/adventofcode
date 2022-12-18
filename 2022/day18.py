# day 18 - voxel surface area
# answer = 4364

# iirc from my old unity project, one solution is to can sweep a 3d grid in 6
# directions (up,down,left,right,front,back) and count exposed faces

def f(a,d,*c):
  e=list(c);
  e[a]+=d;
  return(c in G)and (*e,)not in G
#newline

# voxel grid
# G = [eval(l) for l in open('i/18').readlines()];
G = *map(eval,open('i/18').readlines()),;
# max coordinate in any direction
R=range(max(sum(G,()))+1);

print(
  sum(
      f(a,d,x,y,z)
      for a in (0,1,2)
      for d in (-1,+1)
      for x in R#space
      for y in R#space
      for z in R
  )
)

# c=[x,y,z]
# c[axis]+=dir


#end
exit()


#ORIGINAL CODE

# voxel grid
G = [eval(l) for l in open('i/18').readlines()]

# work out x,y,z ranges
xmin = min(v[0] for v in G)-1 #+-1 so we get the exposed voxels
xmax = max(v[0] for v in G)+1
ymin = min(v[1] for v in G)-1
ymax = max(v[1] for v in G)+1
zmin = min(v[2] for v in G)-1
zmax = max(v[2] for v in G)+1
# @@@ might be able to compress this by just getting the largest magnitude in any direction and going w that
# (will be slower ofc but probs smaller. and looking at the input it's mostly same size in each dir)
# @@@ also can i assume that there's no negatives??? if so minx/y/z can just be 0

ranges=[[xmin,xmax],[ymin,ymax],[zmin,zmax]]

faces_exposed = 0

for axis in 0,1,2:
  for dir in -1,+1:
    # print(ranges[axis][::dir])
    # print(list(range(*ranges[axis][::dir],dir)))
    # @@@ make this a 3D list comprehension
    for x in range(xmin,xmax):
      for y in range(ymin,ymax):
        for z in range(zmin,zmax):
          # is there a voxel at this position?
          c=[x,y,z]
          v0 = tuple(c) in G
          # get the coordinate of the voxel 'above' this voxel in the current sweep direction.
          c[axis]+=dir
          v1 = tuple(c) in G
          faces_exposed += 1 if v0 and not v1 else 0

print(faces_exposed)
