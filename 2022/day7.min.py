def f(s,c,a=0):
 if c=='cd':
  if a[0]<'/':b[0]+=x if(x:=b.pop())<=100000 else 0;b[-1]+=x
  else:b.append(0)
 if s.isdigit():b[-1]+=int(s)
b=[0];[f(*l.split(' '))for l in open('i/7').readlines()];[f('','cd','.')for _ in b];print(b[0])