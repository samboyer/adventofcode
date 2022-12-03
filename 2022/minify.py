import os
import re

def minify(code:str)->str:
    code = re.sub('#.*','', code)
    code = re.sub('\\s*([-+*/:=,])\\s*','\\1', code)
    code = re.sub('\\s*\n\\s*','', code)
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



excludes = ['minify.py']


for file in os.listdir('.'):
    if file.endswith('.py') and not file.endswith('.min.py') and file not in excludes:
        minified = minify(open(file).read())
        with open(file[:-3]+'.min.py','w') as f:
            f.write(minified)

        if len(minified)>PACKER_2_THRESHOLD:
            compressed = compress(minified)
            with open(file[:-3]+'.enc.min.py','wb') as f:
                f.write(bytes(compressed,'u16'))