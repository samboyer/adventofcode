def L(x):return [x]if type(x)==int else x
def e(l,r):
 if[]in[l,r]:return len(l)-len(r)
 a=l[0];b=r[0];t=e(l[1:],r[1:]);return a-b or t if type(a)==type(b)==int else e(L(a),L(b))or t
f=[eval(l)for l in open('i/13').readlines()if l!='\n'];print(sum(i//2+1for i in range(0,len(f),2)if e(f[i],f[i+1])<1))