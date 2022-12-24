# Advent of Code 2022 - sam's extremely cursed solutions

```python
# day 17.min.py - tetris simluator
R=[(0,0)];J=open('i/17').read();j=0;M=lambda:max(c[1]for c in R)
for i in range(2022):
 A=i%5*10;s=[eval(','.join('00102030001001112112001020212200010203000001101100'[r:r+2]))for r in range(A,A+10,2)];x=2;y=M()+4;K=lambda m,n:n and all((m+a,n+b)not in R for a,b in s);L=1
 while L:x+=-(x and K(x-1,y))if J[j%len(J)]<'>'else x<[3,4,4,6,5][i%5]and K(x+1,y);j+=1;L=K(x,y-1);y-=L
 R+=[(x+a,y+b)for a,b in s]
print(M())
```

**Current size of all 2022 programs (days 1-24, pt1): 6,542 bytes (100.3% of github's [favicon.ico](https:/github.com/favicon.ico))**

*(dw i'm gonna fix it)*

Having never tried code golf before (and being a v lazy programmer), I'm gonna try to golf the AoC 2022 problems (see <https://codegolf.meta.stackexchange.com/questions/1280/community-faq-for-programming-puzzles-code-golf> for more info).

Will I get bored 10 days in and give up again? probably yes

## To-do

- pipe code output through cowsay
