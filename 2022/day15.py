# day 15 - manhattan distance beaconing
# answer = 5688618

import re;

print(
    len(
        set.union(*[
            set(
                range(
                    a-(x:=abs(a-c)+abs(b-d)-abs(b-2000000)),
                    a+x
                )
            )
            for a,b,c,d in [
                map(int,re.findall('-?\d+',l))
                for l in open('i/15').readlines()
            ]
        ])
    )
)


# # ORIGINAL CODE
# LOOKUP_Y=2000000

# def f(a,b,c,d):
#     manhattan_dist = abs(a-c)+abs(b-d)
#     y_loss = abs(b-LOOKUP_Y)
#     x_range = manhattan_dist-y_loss
#     # print((a,b),(c,d),manhattan_dist,x_range)
#     return set(range(a-x_range, a+x_range))


# print(
#     len(
#         set.union(*[
#             f(*x)
#             for x in [
#                 map(int,re.findall('-?\d+',l))
#                 for l in open('i/15').readlines()
#             ]
#         ])
#     )
# )


# print([
#     (
#         (a,b),(c,d),
#         (abs(a-c)+abs(b-d)), #mantattan distance
#     )
#     for a,b,c,d in [
#         map(int,re.findall('-?\d+',l))
#         for l in open('i/15.example').readlines()
#     ]
# ])