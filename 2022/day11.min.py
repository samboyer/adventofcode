def k(m):
 for old in m[0]:n=eval(m[1])//3;d=int(m[4]if n%m[2]else m[3]);M[d][0]+=[n];m[5]+=1
 m[0]=[]
M=[[[int(l)for l in t[1][18:].split(',')],t[2][19:],int(t[3][21:]),t[4][29:],t[5][30:],0]for t in[m.split('\n')for m in open('i/11').read().split('\n\n')]];[k(m) for i in [0]*20 for m in M];s=sorted(m[5]for m in M);print(s[-1]*s[-2])