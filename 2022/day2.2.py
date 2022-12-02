# Day 2 - rock paper scissors pt 2 - same as pt1 soln but different lookup table.

# the score of the state "xy" is the index of that sustring in the LUT, //2.
print(
    sum(
        'BXCXAXAYBYCYCZAZBZ'.index(
            l[::2]
        )//2 + 1 for l in open('i/2').readlines()
    )
)

# X = need to lose (0), Y = need to draw (3), Z = need to win (6)
# scores 2={
#     'A X': 0+3,
#     'A Y': 3+1,
#     'A Z': 6+2,
#     'B X': 0+1,
#     'B Y': 3+2,
#     'B Z': 6+3,
#     'C X': 0+2,
#     'C Y': 3+3,
#     'C Z': 6+1,
# };
# scores 2={
#     'B X': 1,
#     'C X': 2,
#     'A X': 3,
#     'A Y': 4,
#     'B Y': 5,
#     'C Y': 6,
#     'C Z': 7,
#     'A Z': 8,
#     'B Z': 9,
# };
# s ='BXCXAXAYBYCYCZAZBZ';
