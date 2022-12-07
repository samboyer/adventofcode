# day 4 - fully-contained sections
# answer=534
import re;
print(
    len(
        [l for l in open('i/4').readlines()
        for a,b,c,d in [map(int,re.split(',|-',l))]
        if (a<=c and b>=d)or(c<=a and d>=b)]
    )
)


# a-b,c-d
# either a<=c and b>=d
# or c<=a and d>=b

# def do(l):
#     a,b,c,d=(int(x) for x in l.replace(',','-').split('-'))
#     return (a<=c and b>=d)or(c<=a and d>=b)


# print(
#     len(
#         [l for l in open('i/4').readlines()
#         if do(l)]
#     )
# )
