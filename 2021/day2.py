f = open('day2.txt')
instrs = f.readlines()
f.close()

x = 0
depth = 0

for i in instrs:
  parts = i.split(' ')
  scale = int(parts[1])
  cmd = parts[0]
  if cmd=='forward':
    x+=scale
  elif cmd=='down':
    depth+=scale
  else: #up
    depth-=scale

print(x, depth)
print(x*depth)

x = 0
depth = 0
aim = 0

for i in instrs:
  parts = i.split(' ')
  scale = int(parts[1])
  cmd = parts[0]
  if cmd=='forward':
    x+=scale
    depth+=aim*scale
  elif cmd=='down':
    aim+=scale
  else: #up
    aim-=scale

print(x, depth, aim)
print(x*depth)