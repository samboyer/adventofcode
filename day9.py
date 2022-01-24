from xml.etree.ElementInclude import include


f = open('day9.txt')
inp = f.readlines()
f.close()

# inp = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""".split('\n') # example data

height = len(inp)
width = len(inp[0]) -1 #exclude '\n'

riskLevel = 0

flooded = [[False]*width for i in range(height)]

basinSizes = []

# returns the number of items filled
def floodFillFrom(startX,startY):
  count=0
  toFill = [(startX, startY)]
  while len(toFill)>0:
    (x,y) = toFill.pop()
    if flooded[y][x]: continue
    flooded[y][x] = True
    count+=1
    if x-1>=0 and inp[y][x-1]!='9' and not flooded[y][x-1]:
      toFill.append((x-1,y))
    if y-1>=0 and inp[y-1][x]!='9' and not flooded[y-1][x]:
      toFill.append((x,y-1))
    if x+1<width and inp[y][x+1]!='9' and not flooded[y][x+1]:
      toFill.append((x+1,y))
    if y+1<height and inp[y+1][x]!='9' and not flooded[y+1][x]:
      toFill.append((x,y+1))

  print(startX,startY,count)
  return count


for y in range(height):
  for x in range(width):
    val = inp[y][x]

    isLow = True
    if x-1>=0: isLow = isLow and inp[y][x-1] > val
    if y-1>=0: isLow = isLow and inp[y-1][x] > val
    if x+1<width: isLow = isLow and inp[y][x+1] > val
    if y+1<height: isLow = isLow and inp[y+1][x] > val

    if isLow:
      riskLevel += 1 + int(val)

      if flooded[y][x]: continue
      basinSizes.append(floodFillFrom(x,y))

print(riskLevel)

basinSizes.sort()
print(basinSizes[-3:])
print(basinSizes[-1]*basinSizes[-2] * basinSizes[-3])