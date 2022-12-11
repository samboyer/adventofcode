# day 11 - monkey in the middle
# answer=55930


# def r(): #newline#space #do a round
#   for m in M:#newline#space#space
#     for old in m[0]: # for each item in this monke's posession (assigned to 'old')
#       n=eval(m[1])//3; #do the new=f(old) expression
#       d = int(m[4]if n%m[2]else m[3]); #work out where this item is going based on divisibility
#       M[d][0]+=[n] #move it there
#       #newline#space#space
#     m[5]+=len(m[0]); #increase items inspected count
#     m[0]=[]


def k(m): #newline#space #do a round for monke m
  for old in m[0]: # for each item in this monke's posession (assigned to 'old')
    n=eval(m[1])//3; #do the new=f(old) expression
    d = int(m[4]if n%m[2]else m[3]); #work out where this item is going based on divisibility
    M[d][0]+=[n]; #move it there
    m[5]+=1 #increase items inspected count
    #newline#space
  m[0]=[]

#newline

M = [
  [
    [int(l)for l in t[1][18:].split(',')], #items in this monke's posession
    t[2][19:], #'new=f(old)' expression
    int(t[3][21:]), #denominator for divisibility test
    t[4][29:], # monke destination if test is True
    t[5][30:], # monke destination if test is False
    0 #number of items inspected by this monke
  ]
  for t in[m.split('\n')for m in open('i/11').read().split('\n\n')]
];

# [r() for i in [0]*20];
[k(m) for i in [0]*20 for m in M]; #run 10 rounds

s=sorted(m[5]for m in M);print(s[-1]*s[-2])

# # INITIAL SOLUTION

# def do_round():
#   for m in monkes:
#     for old in m[0]:
#       n=eval(m[1])//3
#       dst = int(m[4]if n%m[2]else m[3])
#       monkes[dst][0]+=[n]
#     m[5]+=len(m[0])
#     m[0]=[]


# monkes = [
#   [
#     [int(l) for l in txt[1][18:].split(',')], #items in this monke's posession
#     txt[2][19:], #new=f(old) expression
#     int(txt[3][21:]), #denominator for divisibility test
#     txt[4][29:], # monke destination if test is True
#     txt[5][30:], # monke destination if test is False
#     0 #number of items inspected by this monke
#   ]
#   for txt in[t.split('\n') for t in open('i/11').read().split('\n\n')]
# ];

# [do_round() for i in [0]*20]

# s=sorted(m[5]for m in monkes)[-2:];print(s[-1]*s[-2])


# early code

# txts=[t.split('\n') for t in open('i/11.example').read().split('\n\n')]
# monkes = [
#   [
#     [int(l) for l in txt[1][18:].split(',')], #items in this monke's posession
#     txt[2][19:], #new=f(old) expression
#     int(txt[3][21:]), #denominator for divisibility test
#     txt[5][30:], #'if true' address
#     txt[4][29:]
#   ]
#   for txt in txts
# ]

# for txt in txts:
#   print(txt[1][18:])
#   for old in (int(l) for l in txt[1][18:].split(',')): #for each item in this monke's posession,
#     n=eval(txt[2][19:])//3 #extract the 'old+n' operation, eval it as python code, assign to n
#     # print(old,n)
#     dst=txt[5][30:]if n%int(txt[3][21:])else txt[4][29:]  #(inverted to avoid '==0')
#     print(dst)
