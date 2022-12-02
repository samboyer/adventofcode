# Day 2 - rock paper scissors
s = [
    'B X',
    'C Y',
    'A Z',
    'A X',
    'B Y',
    'C Z',
    'C X',
    'A Y',
    'B Z'
];

print(
    sum(s.index(l.strip())+1 for l in open('i/2').readlines())
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