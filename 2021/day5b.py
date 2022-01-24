f = open('day5.txt')
lines = f.readlines()
f.close()

vents = []

for l in lines:
  coords = l.split(' -> ')
  s = coords[0].split(',')
  e = coords[1].split(',')
  vents.append(
    ((int(s[0])-1, int(s[1])-1),
    (int(e[0])-1, int(e[1])-1))
  )

# determine grid dimensions
maxX = 0
maxY = 0
for v in vents:
  maxX = max(maxX, v[0][0], v[1][0])
  maxY = max(maxY, v[0][1], v[1][1])

grid = [[0]*(maxX+1) for j in range(0, maxY+1)]

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
  else: #diagonal
    minX = min(v[0][0], v[1][0])
    maxX = max(v[0][0], v[1][0])
    isAscendng = (v[1][1] > v[0][1]) if v[0][0] < v[1][0] else  (v[1][1] < v[0][1])
    j = v[0][1] if v[0][0] < v[1][0] else v[1][1]
    inc = 1 if isAscendng else -1
    for i in range(minX, maxX+1):
      grid[j][i] += 1
      j += inc

# count points with overlap
c = 0
for row in grid:
  for cell in row:
    if cell>1: c+=1
print(c)

print("Count of all overlaps: "+str(c))

