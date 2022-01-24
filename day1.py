f = open('day1.txt')
nums = f.readlines()
f.close()

def countIncreasesIn(arr):
  last = 100000000
  count = 0
  for l in arr:
    num = int(l)

    if num>last:
      count+=1
    last = num
  return count

print(countIncreasesIn(nums))

# part 2
slidingWindows = []
for i in range(0, len(nums)-2):
  s = int(nums[i]) + int(nums[i+1]) + int(nums[i+2])
  slidingWindows.append(s)

print(countIncreasesIn(slidingWindows))