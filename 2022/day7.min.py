def f(c):
 global b,t
 if c[1]=='cd':
  if c[2][0]=='.':t+=x if(x:=b.pop())<=100000 else 0;b[-1]+=x
  else:b+=[0]
 b[-1]+=int(c[0])if c[0].isdigit()else 0
b=[];t=0;[f(l.split(' '))for l in open('i/7').readlines()];[f(['','cd','.'])for _ in b];print(t)