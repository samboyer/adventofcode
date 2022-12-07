# day 7 pt 2 - directory traversal - deleting files
# answer = 4443914

def f(c):#newline#space
    global b,r,s#newline#space
    if c[1]=='cd':#newline#space#space
        if c[2][0]=='.':
            x=b.pop();
            s=min(s,x)if x>r else s;
            b[-1]+=x#newline#space#space
        else:
            b+=[0] #push 0 to subdir size stack
            #newline#space
    b[-1]+=int(c[0])if c[0].isdigit()else 0
#newline

s=9**9;
b=[]; #stack of subdirectory sizes
z=open('i/7').readlines();

r = sum(int(l.split()[0])for l in z if l[0].isdigit())-4*10**7; #amount of space we need to delete
[f(l.split(' '))for l in z];
[f(['','cd','.'])for _ in b]; #insert extra 'cd ..'s to sum up the remaining entries
print(s)

# remaining_space = (7k -used_space)
# to_delete = 3k - remaining_space
# =3k-(7k-used_space)
# = used_space-4k




# s=[l.replace('$ ','').split(' ') for l in open('i/7').readlines()[1:]] #skip 'cd /', remove $s


# option 1:
# convert command sequence into hierarchy of dicts
# then recurse thru the dicts and sum their sizes
# OR  sum the sizes on the fly (option 2)
# both will need to maintain a stack representing cwd;
# option 2 will need a stack of sizes(?)
# >>>option 2 relies on the asusmption that a directory is not entered twice<<<


# command parsing:
# (\d+) [filename] : ignore filename, add $1 to directory total
# dir [dirname] : ignore line; we can't get any info from this.
# cd [dirname]:
#   - ~~push dirname to directory stack~~ not needed
#   -  push 0 to size stack
# cd .. :
#   - ~~pop dirname from directory stack~~ not needed
#   - pop size from size stack
#   - if size<=100000, add size to total
#   - add size to top of size stack (ie of parent directory)
# note that at the end of the instructions, we also need to run the 'cd ..' routine until the end.



# def f_stateless(b,t,c):
#     if c[0]=='cd':
#         if c[1]=='..\n':
#             if (x:=b.pop())<=100000:
#                 return (b[:-1],t+x)
#             else:
#                 return (b[:-1],t)
#         else:
#             return (b+[0],t)
#     else:
#         if c[0].isdigit():
#             return (b[:-1]+[b[-1]+int(c[0])],t)
#         else:
#             return (b,t)

# # f as a lambda:
# f = lambda b,t,c: (((b[:-1],t+x)if(x:=b.pop())<=100000 else (b[:-1],t))if c[1]=='..\n' else (b+[0],t)) if c[0]=='cd'else ((b[:-1]+[b[-1]+int(c[0])],t) if c[0].isdigit() else (b,t))


# import functools as z
# print(
#     z.reduce(
#         lambda b,t,c: (((b[:-1],t+x)if(x:=b.pop())<=100000 else (b[:-1],t))if c[1]=='..\n' else (b+[0],t)) if c[0]=='cd' else ((b[:-1]+[b[-1]+int(c[0])],t) if c[0].isdigit() else (b,t)),
#         [l.replace('$ ','').split(' ') for l in open('i/7').readlines()[1:]],
#         ([0],0),
#     )
# )