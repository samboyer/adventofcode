# day 21 - monkey evaluation
# answer = 331120084396440

import re;

exec(
  re.sub(
    '([a-z]+)',
    '\\1()',
    open('i/21').read()
  ).replace('():','=lambda:')
);


print(root())