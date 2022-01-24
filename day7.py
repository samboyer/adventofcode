f = open('day7.txt')
inp = f.readline()
f.close()

# inp = '16,1,2,0,4,2,7,1,2,14' # example data

positions = [int(x) for x in inp.split(',')]

minX = min(positions)
maxX = max(positions)

print("== Part 1 ==")
currentBestX = -1
currentBestCost = 1000000000000000000000000

for x in range(minX, maxX):
  cost = 0
  for pos in positions:
    cost+=abs(pos-x)
    if cost>currentBestCost: break
  if cost<currentBestCost:
    currentBestX = x
    currentBestCost = cost

print("Cheapest position = {}, cost = {}".format(currentBestX, currentBestCost))

print("== Part 2 ==")
currentBestX = -1
currentBestCost = 1000000000000000000000000

for x in range(minX, maxX):
  cost = 0
  for pos in positions:
    dist = abs(pos-x)
    if dist>0:
      cost += dist*(1+dist)/2
    if cost>currentBestCost: break
  if cost<currentBestCost:
    currentBestX = x
    currentBestCost = cost

print("Cheapest position = {}, cost = {}".format(currentBestX, int(currentBestCost)))
