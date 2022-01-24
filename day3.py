f = open('day3.txt')
lines = f.readlines()
f.close()
numLines = len(lines)

bitLength = len(lines[0].strip())
countOfOnesInThisIndex = [0]*bitLength

def recalculateCountOfOnesOn(arr):
  countOfOnesInThisIndex = [0]*bitLength
  for l in arr:
    for i in range(0, bitLength):
      if l[i]=='1':
        countOfOnesInThisIndex[i]+=1
  return countOfOnesInThisIndex

countOfOnesInThisIndex = recalculateCountOfOnesOn(lines)

gammaBin = ''
epsilonBin = ''

for c in countOfOnesInThisIndex:
  if(c>numLines/2):
    gammaBin+='1'
    epsilonBin+='0'
  else:
    gammaBin+='0'
    epsilonBin+='1'

gammaRate = int(gammaBin, 2)
epsilonRate = int(epsilonBin, 2)

print(gammaRate, epsilonRate)
print(gammaRate*epsilonRate)

potentialOxVals  = lines

for i in range(0, bitLength):
  if len(potentialOxVals)==1: break
  newOx = []
  print(countOfOnesInThisIndex[i], numLines/2)

  if(countOfOnesInThisIndex[i]>=numLines/2): #1 is more common or equal
    #only keep 1s in ox, only keep 0s in co2
    newOx = [x for x in potentialOxVals if x[i] == '1']
  else: #0 is more common
    #only keep 0s in ox, only keep 1s in co2
    newOx = [x for x in potentialOxVals if x[i] == '0']

  potentialOxVals = newOx
  countOfOnesInThisIndex = recalculateCountOfOnesOn(newOx)
  numLines = len(newOx)

potentialCO2Vals = lines
countOfOnesInThisIndex = recalculateCountOfOnesOn(lines)
numLines = len(lines)

for i in range(0, bitLength):
  if len(potentialCO2Vals)==1: break
  newCO2 = []
  print(countOfOnesInThisIndex[i], numLines/2)

  if(countOfOnesInThisIndex[i]>=numLines/2): #1 is more common or equal
    #only keep 1s in ox, only keep 0s in co2
    newCO2 = [x for x in potentialCO2Vals if x[i] == '0']
  else: #0 is more common
    #only keep 0s in ox, only keep 1s in co2
    newCO2 = [x for x in potentialCO2Vals if x[i] == '1']
  potentialCO2Vals = newCO2
  countOfOnesInThisIndex = recalculateCountOfOnesOn(newCO2)
  numLines = len(newCO2)

oxBits = potentialOxVals[0]
co2Bits = potentialCO2Vals[0]

print(oxBits, co2Bits)

oxGenRating = int(oxBits, 2)
co2Rating = int(co2Bits, 2)

print(oxGenRating, co2Rating)
print(oxGenRating*co2Rating)


