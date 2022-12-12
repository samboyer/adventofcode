# Advent of Code 2022 - sam's extremely cursed solutions

```python
# day11.2.min.py - monkey throwing simulation
def k(m):
 for old in m[0]:n=eval(m[1])%prod(m[2]for m in M);d=int(m[4]if n%m[2]else m[3]);M[d][0]+=[n];m[5]+=1
 m[0]=[]
from math import prod;M=[[[int(l)for l in t[1][18:].split(',')],t[2][19:],int(t[3][21:]),t[4][29:],t[5][30:],0]for t in[m.split('\n')for m in open('i/11').read().split('\n\n')]];[k(m) for i in [0]*10000 for m in M];print(prod(sorted(m[5]for m in M)[-2:]))
```

Having never tried code golf before (and being a v lazy programmer), I'm gonna try to golf the AoC 2022 problems (see <https://codegolf.meta.stackexchange.com/questions/1280/community-faq-for-programming-puzzles-code-golf> for more info).

Will I get bored 10 days in and give up again? probably yes

## To-do

- pipe code output through cowsay
