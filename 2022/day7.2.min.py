def f(c):
 global b,r,s
 if c[1]=='cd':
  if c[2][0]=='.':x=b.pop();s=min(s,x)if x>r else s;b[-1]+=x
  else:b+=[0]
 b[-1]+=int(c[0])if c[0].isdigit()else 0
s=9**9;b=[];z=open('i/7').readlines();r=sum(int(l.split()[0])for l in z if l[0].isdigit())-4*10**7;[f(l.split(' '))for l in z];[f(['','cd','.'])for _ in b];print(s)