# day 5 - supply stacks
# answer=FWSHSPJWM

f=open('i/5').readlines();
a=f.index('\n');

# extract stacks from textual representation
s=[' ']+[[l[i]for l in f[:a]if l[i]!=' ']for i in range(1,len(f[0]),4)] #newline

# replay parsed instructions
for n,x,y in[
    [
        int(i)
        for i in l.split() #split into words, filter to ints only
        if i.isdigit()]
        for l in f[a+1:] #each instruction line
    ]:
    # reverse portion of stack x and put it on stack y
    s[y]=s[x][:n][::-1]+s[y];
    del s[x][:n]
    #newline
print(''.join(l[0]for l in s))


# # extract rows from stack textual representation
# r = [l[1::4] for l in f[:a]]
# # transpose to get list of stacks
# s = [[c[i] for c in r if c[i]!=' '] for i in range(len(r[0]))]

# # parse instructions
# o = [[int(i) for i in l.split() if i.isdigit()] for l in f[a+1:]]


# # replay instructions
# for n,x,y in o:
#     # lift a portion of stack x
#     p=s[x][:n];
#     del s[x][:n];
#     # reverse it and put it on stack y
#     s[y]=p[::-1]+s[y];