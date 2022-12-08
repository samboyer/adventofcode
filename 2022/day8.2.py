# day 8 pt 2 - tree visibility
# answer = 211680

g = open('i/8','rb').readlines();
n = range(len(g));

# transpose grid for easier vertical lookups
t =[[r[i]for r in g]for i in n];

from math import prod#newline

# REFACTOR: remove last element from every line-of-sight because we always want to consider the edge of the grid as a 'hit'

print(
    max(
        prod( #list product
            ([x>=g[j][i]for x in s]+[1]).index(1)+1
            for s in [
                g[j][1:i][::-1], #going left
                g[j][i+1:-2],   #going right (excluding newline)
                t[i][1:j][::-1], #going up
                t[i][j+1:-1]      #going down
            ]
        )
        for i in n#space
        for j in n
    )
)


# [x>=g[j][i]for x in s].get(1, len(s)-1)+1


# print(
#     max(
#         p( #list product
#             min(
#                 ([x>=g[j][i]for x in s]+[1]).index(1)+1,
#                 len(s) #so that 'going off the edge of the grid' is handled properly
#             ) for s in [
#                 g[j][:i][::-1], #going left
#                 g[j][i+1:-1],   #going right (excluding newline)
#                 t[i][:j][::-1], #going up
#                 t[i][j+1:]      #going down
#             ]
#         )
#         for i in n#space
#         for j in n
#     )
# )


# # g is grid, t is transposed grid, x,y are tree coords
# def visible(x,y):
#     h = g[y][x]
#     return (all(i<h for i in g[y][:x])
#         or all(i<h for i in g[y][x+1:])
#         or all(i<h for i in t[x][:y])
#         or all(i<h for i in t[x][y+1:])
#     )