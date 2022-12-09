# day 9 - rope movement
# answer=6311


# x,y coords of head/tail
t=(h:=[0,0])[:];

# # mapping of directions to operations:
# o={'U':'h[1]+=1','D':'h[1]-=1','L':'h[0]-=1','R':'h[0]+=1'},
# removed common prefix+suffix:
O={'U':'1]+','D':'1]-','L':'0]-','R':'0]+'}

#newline

def f(d):#newline#space
    # print(d)
    exec(f'h[{O[d]}=1'); #make the right head movement

    x=h[0]-t[0];
    y=h[1]-t[1]#newline#space

    if y>1:
        t[1]+=1;
        #if there's also an x difference, allow to move diagonally.
        #(assuming we're moving correctly, x will only ever be [-1..1])
        t[0]+=x#newline#space
    if y<-1:
        t[1]-=1;
        t[0]+=x#newline#space
    if x>1:
        t[0]+=1;
        t[1]+=y#newline#space
    if x<-1:
        t[0]-=1;
        t[1]+=y#newline#space
    return tuple(t) #return tail pos to make set of unique tail positions
#newline

print(
    len(
        set(
            f(d)
            for l in open('i/9').readlines()
            for d in l[0]*int(l[2:]) # replace 'X n' with 'XXX...X'
        )
    )
)

# def f(d):
#     # print(d)
#     exec(f'h[{O[d]}=1'); #make the right head movement
#     m() #call tail catchup function
#     return tuple(t) #return tail pos to make set of unique tail positions


# def m():
#     # catch up head with tail
#     # print(f'h={h},t={t}')
#     dx=h[0]-t[0];
#     dy=h[1]-t[1];
#     # print(f'dx={dx},dy={dy}')
#     if dy>1:
#         t[1]+=1
#         t[0]+=dx #if there's also an d difference, allow to move diagonally.
#             #(assuming we're moving correctly, dx will only ever be [-1..1])
#     if dy<-1:
#         t[1]-=1
#         t[0]+=dx
#     if dx>1:
#         t[0]+=1
#         t[1]+=dy
#     if dx<-1:
#         t[0]-=1
#         t[1]+=dy
#     # print(f'new t={t}')


# early ideas for movement funcs

# def U(h):h[1]+=1#newline
# def D(h):h[1]-=1#newline
# def L(h):h[0]-=1#newline
# def R(h):h[0]+=1#newline

# U=lambda:(hy:=hy+1)
# D=lambda:(hy:=hy-1)
# L=lambda:(hx:=hx-1)
# R=lambda:(hx:=hx+1)

# X={'U':0,'D':0,'L':-1,'R':1}
# Y={'U':0,'D':0,'L':-1,'R':1}
# hx+=X[l[0]];hy+=X[l[0]]