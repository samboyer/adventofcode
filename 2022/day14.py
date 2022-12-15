# day 14 - sand simulation
# answer = 858

# set of coordinates containing a rock, or sand
R = [
    (x,y) for (a,b),(c,d) in [ # wall segments
        sorted(p) # make sure the lower (lexicographic) end comes first
        for w in [ #walls
            [*map(
                eval, #convert comma separated list to int tuple :)
                l.split('->')
            )]
            for l in open('i/14').readlines()
        ]
        for p in zip(w,w[1:])
    ]
    for x in range(a,c+1)
    for y in range(b,d+1)
];
# print(R)

M = max(c[1] for c in R);
# print(max_y)

i=0 # sand grain count

#newline

# starts at 500,0. if grain stops on the ground, edit rocks list, return True.
# if grain reaches max_y (ie the abyss), return false
def f(x,y):
    Y=y+1;
    return y<M and (
        (
            (
                # (
                    R.append((x,y)) or True#space
                # )
                if (x+1,Y) in R#space
                else f(x+1,Y)
            )
            if (x-1,Y) in R#space
            else f(x-1,Y)
        )
    if (x,Y) in R#space
    else f(x,Y)
    )

#newline

while f(500,0):i+=1
#newline
print(i)


# # PRE-GOLFED CODE

# walls = [
#     [list(map(int,c.split(','))) for c in l.split('->')]
#     for l in open('i/14').readlines()
# ]
# segments = [p if p[0]<p[1]else(p[1],p[0])for w in walls for p in zip(w,w[1:])]
# # print(segments)

# rocks = [
#     (x,y) for s in segments
#     for x in range(s[0][0],s[1][0]+1)
#     for y in range(s[0][1],s[1][1]+1)
# ]
# # print(rocks)
# max_y = max(c[1] for c in rocks)
# # print(max_y)

# # is this coordinate a ground piece?
# def g(x,y):return (x,y) in rocks


# # starts at 500,0. if grain stops on the ground, edit rocks list, return True.
# # if grain reaches max_y (ie the abyss), return false
# def fall(x,y):
#     if g(x,y+1):
#         if g(x-1,y+1):
#             if g(x+1, y+1):
#                 rocks.append((x,y))
#                 return True
#             else: return y+1<max_y and fall(x+1,y+1)
#         else: return y+1<max_y and fall(x-1,y+1)
#     else:
#         return y+1<max_y and fall(x,y+1)
#     return y==max_y


# i=0 # sand grain count
# while(fall(500,0)):
#     i+=1
# print(i)


# # OLD IDEA - doesn't work bc of double includes. possibly a
# # dynamic programming solution would fix it?
# # can we do a recursive fn(coord) that returns (bool,int)
# # ie. whether the abyss is not reached from this coord  and
# # the number of sands that can be dropped from this coord?
# def f(x,y):
#     if g(x,y):return (True,0)
#     if y==max_y:return (False,0)
#     a=b=c=0
#     abyss_not_reached_yet, a = f(x,y+1)
#     if abyss_not_reached_yet: abyss_not_reached_yet, b = f(x-1,y+1)
#     if abyss_not_reached_yet: abyss_not_reached_yet, c = f(x+1,y+1)
#     print(x,y,abyss_not_reached_yet, a+b+c)
#     return (abyss_not_reached_yet, a+b+c+1)