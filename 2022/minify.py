import os
import re

DO_COMPRESSION = False

SUBS = {
    '#end\\n(\\n|.)*': '', #macro to remove the rest of the file
    '#newline': '@newline@', #for when we actually need a newline (e.g. ending a for loop)
    '#space': '@space@',  #for when we actually need a space (e.g. indenting a nested if statement)
    '\\s*([^\'"])#.*': '\\1',
    '^#.*': '',
    '\\s*([-+*/:=,])\\s*': '\\1',
    '\\s*\n\\s*': '',
    '([)\\]}])\\s*(\\w)': '\\1\\2',
    '(\\w)\\s*([[([{])': '\\1\\2',
    # reinsert special statements
    '@newline@': '\n',
    '@space@': ' ',
    # cleanup
    '\\s+\n': '\n',
    '\\s+$': '\n',
    '\r': '', #convert from CRLF to LF
}

def minify(code:str)->str:
    for find, repl in SUBS.items():
        code = re.sub(find,repl,code)
    return code

PACKER_2_THRESHOLD = 50
PACKER_3_THRESHOLD = 73

# courtesy of https://code.golf/wiki/langs/python
def crt(a, n):
	s, p = 0, 1
	for x in n:
		p *= x
	for x, y in zip(a, n):
		q = p // y
		s += q * x * pow(q, -1, y)
	return s % p

def compress(code:str)->bytes:
    # python code compressors, courtesy of https://code.golf/wiki/langs/python
    if False and len(code) > PACKER_3_THRESHOLD:
        # 3:1 packer
        compressed = ''
        for i in range(0, len(code), 3):
            a = [ord(c) - 32 for c in code[i:i+3]]
            compressed += chr(crt(a, [101, 102, 103]))
        return f"exec(bytes(ord(c)%i+32for c in'{compressed}'for i in b'efg'))"

    elif len(code) > PACKER_2_THRESHOLD:
        # 2:1 packer
        encoded = code.encode().decode('u16')
        return f"exec(bytes('{encoded}','u16')[2:])"



excludes = ['minify.py','count.py']

files={}

for file in os.listdir('.'):
    if file.endswith('.py') and not file.endswith('.min.py') and file not in excludes:
        minified = minify(open(file).read())
        if '.2.' not in file:
            day=int(file[3:-3])
            files[day]=minified

        with open(file[:-3]+'.min.py','wb') as f:
            f.write(minified.encode('ASCII'))


        if DO_COMPRESSION and len(minified)>PACKER_2_THRESHOLD:
            compressed = compress(minified)
            with open(file[:-3]+'.enc.min.py','wb') as f:
                f.write(bytes(compressed,'u16'))



combined="""from collections import deque
import re
_r=range
_p=print
_u=lambda f:open(f).read()
_v=lambda f:open(f).readlines()
"""

ALL_SUBS = {
  'range':'_r',
  'print':'_p',
  'open\(([i/0-9\']+)\).read\(\)' : '_u(\\1)',
  'open\(([i/0-9\']+)\).readlines\(\)' : '_v(\\1)',
  'import re(;|\n)' : '',
  'from collections import deque(;|\n)' : '',
}


for name,code in sorted(files.items(), key=lambda item: item[0]):
    for find, repl in ALL_SUBS.items():
        code = re.sub(find,repl,code)
    combined+=code+'\n'


print(f'all.min.py file is {len(combined)} bytes!')
open('all.min.py','wb').write(combined.encode('ASCII'))