f=open('i/5').readlines();a=f.index('\n');s=[' ']+[[l[i]for l in f[:a]if l[i]!=' ']for i in range(1,len(f[0]),4)]
for n,x,y in[[int(i)for i in l.split()if i.isdigit()]for l in f[a+1:]]:s[y]=s[x][:n]+s[y];del s[x][:n]
print(''.join(l[0]for l in s))