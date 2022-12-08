# day 8 - tree visibility
# answer = 1823

g = open('i/8','rb').readlines();
n = range(len(g));

# transpose grid for easier vertical lookups
t =[[r[i]for r in g]for i in n];

print(
    sum(
        [
            any(
                all(
                    x<g[j][i]
                    for x in s
                )for s in[
                g[j][:i],
                g[j][i+1:],
                t[i][:j],
                t[i][j+1:]
            ])
            for i in n#space
            for j in n
        ]
    )
)


# # g is grid, t is transposed grid, x,y are tree coords
# def visible(x,y):
#     h = g[y][x]
#     return (all(i<h for i in g[y][:x])
#         or all(i<h for i in g[y][x+1:])
#         or all(i<h for i in t[x][:y])
#         or all(i<h for i in t[x][y+1:])
#     )