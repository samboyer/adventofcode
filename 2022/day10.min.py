def f(i):global X;X+=i;return[X-i,X-i]
X=1;print(sum([i*x for i,x in enumerate(sum((f(int(l[4:]))if 'a' in l else [X] for l in open('i/10').readlines()),[0]))][20::40]))