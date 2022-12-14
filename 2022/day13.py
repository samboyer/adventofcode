# day 13 - nested array comparison
# answer in 5390

def L(x): #listify x
    return [x]if type(x)==int else x

#newline

def e(l,r):#newline#space
    if[]in[l,r]:return len(l)-len(r)#newline#space
    a=l[0];b=r[0];
    t=e(l[1:],r[1:]);
    return a-b or t if type(a)==type(b)==int else e(L(a),L(b))or t

#newline


# list of arrays
f=[eval(l)for l in open('i/13').readlines()if l!='\n'];

# for i in range(0,len(f),2):
#     print(f[i])
#     print(f[i+1])
#     print(i//2+1, t(f[i],f[i+1]))
#     print(e(f[i],f[i+1]))
#     print()

print(
    sum(
        i//2+1
        for i in range(0,len(f),2)
        if e(f[i],f[i+1])<1
    )
)


# def e(l,r):
#     a=l[0];b=r[0]
#     # returns -1 if l<r, 0 if l==r, 1 otherwise
#     if l==[] or r==[]: return len(l)-len(r)
#     t=e(l[1:],r[1:])
#     # both lists have at least one elem.
#     # if both elems are ints, return the difference. if the diff is 0 (ie equal), return the diff of the tail
#     if type(a)==int and type(a)==int: return a-b or t
#     # if either is a list, listify both heads, check the diff; if they're equal, return the diff of the tail
#     return e(L(a),L(b)) or t

# def t(l,r):
#     # print(l,r)
#     # returns true if in the right order (l,r), false otherwise
#     if l==[]: return True
#     if r==[]: return False
#     # both lists have at least one elem.
#     if type(l[0])==int and type(r[0])==int: return l[0]<r[0] or (l[0]<=r[0] and t(l[1:],r[1:]))
#     return t(L(l[0]),L(r[0])) and t(l[1:],r[1:])
#     # return t([l[0]],r[0]) and t(l[1:],r[1:]) # if left head is int, right is list
#     # return t(l[0],[r[0]]) and t(l[1:],r[1:]) # if left head is list, right is int
#     # return t(l[0],r[0]) and t(l[1:],r[1:]) # both lists
