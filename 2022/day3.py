# Day 3 - rucksack packing

print(
  sum(
    26+(c&31)-(c&32 and 26)
    for c in [
      [l for l in s[:len(s)//2] if l in s[len(s)//2:]][0]
      for s in open('i/3','rb').readlines()
    ]
  )
)


# def letter_to_priority(c):
#   return c - 64+26 if c<96 else c-96
# # (ascii decimal values of 'A' and 'a', )

# def letter_to_priority_2(c):
#   return (c&31)+(0 if c&32 else 26)
# # (5 least significant bits, plus 26 if it's a capital letter (when bit 32 NOT set))

# def letter_to_priority_3(c):
#   return 26+(c&31)-(c&32and 26)
# # (5 least significant bits, minus 26 bit 32 set, plus 26


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

# answer = 7793