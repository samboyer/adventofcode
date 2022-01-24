f = open('day5.txt')
lines = f.readlines()
f.close()

vents = []

for l in lines:
  coords = l.split(' -> ')
  s = coords[0].split(',')
  e = coords[1].split(',')
  vents.append(
    ((int(s[0]), int(s[1])),
    (int(e[0]), int(e[1])))
  )

# determine grid dimensions
maxX = 0
maxY = 0
for v in vents:
  maxX = max(maxX, v[0][0], v[1][0])
  maxY = max(maxY, v[0][1], v[1][1])

grid = [[0]*maxX for j in range(0, maxY)]

# populate grid
for v in vents:
  isAxisAligned = (v[0][0] == v[1][0]) or (v[0][1] == v[1][1])

  if isAxisAligned:
    isHorizontal = (v[0][1] == v[1][1])
    if isHorizontal:
      y = v[0][1]
      start = min(v[0][0], v[1][0])
      end   = max(v[0][0], v[1][0])
      for i in range(start, end+1):
        grid[y][i] += 1
    else: # vertical
      x = v[0][0]
      start = min(v[0][1], v[1][1])
      end   = max(v[0][1], v[1][1])
      for j in range(start, end+1):
        grid[j][x] += 1

# count points with overlap
count = 0
for j in range(0, maxY):
  for i in range(0, maxX):
    if(grid[j][i]>1): count+=1

print("Count of axis-aligned overlaps: "+str(count))

