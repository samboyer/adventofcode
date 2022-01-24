# one element for each fish won't work for large counts,
# so instead keep a count of how many fish have each value,
# then sum all the entries.

f = open('day6.txt')
inp = f.readline()
f.close()

initialFishes = [int(x) for x in inp.split(',')]
fishCounts = {i:initialFishes.count(i) for i in range(0, 8+1)}
print(fishCounts)

maxDays = 256
for d in range(1, maxDays+1):
  #shift nums 1-8 down by 1
  newFishCounts = {(i-1):fishCounts[i] for i in range(1, 8+1)}
  # convert num 0 into a 6 and 8
  newFishCounts[8] = fishCounts[0]
  newFishCounts[6] += fishCounts[0]

  # print(newFishCounts)
  fishCounts = newFishCounts

finalCount = sum(fishCounts.values())
print("Fish count after {} days: {}".format(maxDays, finalCount))