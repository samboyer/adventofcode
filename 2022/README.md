# Advent of Code 2022 - sam's extremely cursed solutions

```python
# day5.min.py
f=open('i/5').readlines();a=f.index('\n');s=[' ']+[[l[i]for l in f[:a]if l[i]!=' ']for i in range(1,len(f[0]),4)]
for n,x,y in[[int(i)for i in l.split()if i.isdigit()]for l in f[a+1:]]:s[y]=s[x][:n][::-1]+s[y];del s[x][:n]
print(''.join(l[0]for l in s))
```

Having never tried code golf before (and being v lazy), I've rather impulsively decided to solve them using as few characters of python3 code as possible (i.e. code golf - see <https://github.com/samboyer/adventofcode.git>).

Will I get bored 10 days in and give up again? probably yes

## To-do

- pipe code output through cowsay
