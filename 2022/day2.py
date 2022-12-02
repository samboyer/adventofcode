# Day 2 - rock paper scissors

# the score of the state "xy" is the index of that sustring in s, //2.
s = 'BXCYAZAXBYCZCXAYBZ';

print(
    sum(
        s.index(
            l[::2]
        )//2 + 1 for l in open('i/2').readlines()
    )
)


# scores={
#     'A X': 3+1,
#     'A Y': 6+2,
#     'A Z': 0+3,
#     'B X': 0+1,
#     'B Y': 3+2,
#     'B Z': 6+3,
#     'C X': 6+1,
#     'C Y': 0+2,
#     'C Z': 3+3,
# };

# VVVV

# states are indexed by their score
# s = [
#     'B X',
#     'C Y',
#     'A Z',
#     'A X',
#     'B Y',
#     'C Z',
#     'C X',
#     'A Y',
#     'B Z'
# ];

# VVVV

# the score of the state "x y" is the index of that sustring in string `s`, //3.
# s = 'B XC YA ZA XB YC ZC XA YB Z';