# Advent of Code 2022 - sam's extremely cursed solutions

```python
# day5.min.py - cargo stack manipulation
f=open('i/5').readlines();a=f.index('\n');s=[' ']+[[l[i]for l in f[:a]if l[i]!=' ']for i in range(1,len(f[0]),4)]
for n,x,y in[[int(i)for i in l.split()if i.isdigit()]for l in f[a+1:]]:s[y]=s[x][:n][::-1]+s[y];del s[x][:n]
print(''.join(l[0]for l in s))
```

Having never tried code golf before (and being a v lazy programmer), I'm gonna try to golf the AoC 2022 problems (see <https://codegolf.meta.stackexchange.com/questions/1280/community-faq-for-programming-puzzles-code-golf> for more info).

Will I get bored 10 days in and give up again? probably yes

## To-do

- pipe code output through cowsay
