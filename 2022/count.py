
import os
n=0
sizes={}
for name in os.listdir('.'):
  if '.min.py' in name and '.2.' not in name:
    size=len(open(name,'rb').read())
    sizes[name]=size
    n+=size

for name,size in sorted(sizes.items(), key=lambda item: item[1]):
    print(name,size)

favicon=6518
print(f"Size of all .min files: {n} bytes ({n/favicon*100}%)")
