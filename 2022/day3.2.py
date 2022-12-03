# Day 3 - rucksack packing - part 2 (badge finding)
# answer = 2499

l=open('i/3','rb').readlines();
print(
  sum(
    26+(c&31)-(c&32 and 26)
    for c in [
      [b for b in l[i] if b in l[i+1] and b in l[i+2]][0]
      for i in range(0,len(l),3)
    ]
  )
)



# def find_badge(t):
#   return [l for l in t[0] if l in t[1] and l in t[2]]



# def letter_to_priority(c):
#   return c - 64+26 if c<96 else c-96
# # (ascii decimal values of 'A' and 'a', )

# def letter_to_priority_2(c):
#   return (c&31)+(0 if c&32 else 26)
# # (5 least significant bits, plus 26 if it's a capital letter (when bit 32 NOT set))

# def letter_to_priority_3(c):
#   return 26+(c&31)-(c&32and 26)
# # (5 least significant bits, minus 26 bit 32 set, plus 26

# l=open('i/3','rb').readlines();
# print(sum(
#   letter_to_priority_3(find_badge(l[i:i+3])[0])
#   for i in range(0,len(l),3)
# )
# )

# def item_in_both(s):
#   l=len(s)//2
#   h1 = s[:l]
#   h2 = s[l:]
#   dups = [c for c in h1 if c in h2]
#   return dups

# def item_in_both_2(s):
#   return [c for c in s[:len(s)//2] if c in s[len(s)//2:]]


# def solution():
#   print(
#     sum(
#       letter_to_priority_3(c[0])
#       for c in [
#         item_in_both(s)
#         for s in open('i/3','rb').readlines()
#       ]
#     )
#   )

