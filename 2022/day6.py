# day 6 - marker finding
# answer=1855

# 'identify the first position where the four most recently received characters were all different'

s=open('i/6').read();
print([len(set(s[i:i+4])) for i in range(len(s))].index(4)+4)

# early versions

# s=open('i/6').read();
# print(list(map(lambda i:len(set(s[i:i+4])), range(len(s)))).index(4)+4)

# for i in range(len(s)):
#     if len(set(s[i:i+4]))==4:
#         print(i+4)
#         exit()


# s=open('i/6').read()
# for i in range(len(s)):
#     if len(set(s[i:i+4]))==4:
#         print(i+4);
#         break
