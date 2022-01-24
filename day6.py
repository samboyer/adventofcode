f = open('day6.txt')
inp = f.readline()
f.close()

fishes = [int(x) for x in inp.split(',')]

maxDays = 80

# print("Initial state: {}".format(str(fishes)))

for d in range(1, maxDays+1):
  fishesThisGen = len(fishes)
  print(d, fishesThisGen)
  for i in range(0, fishesThisGen):
    if fishes[i] == 0:
      fishes[i] = 6
      fishes.append(8)
    else:
      fishes[i]-=1

  # print("After {} days: {}".format(d, str(fishes)))

print("Fish count after {} days: {}".format(maxDays, len(fishes)))