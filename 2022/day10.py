# day 10 - signal strength
# answer=12840

def f(i):global X;X+=i;return[X-i,X-i]
#newline

X=1;
print(
  sum(
    [
      i*x#space
      for i,x in enumerate(
        sum(
          (
            f(int(l[4:]))
            if 'a' in l#space
            else [X]#space
            for l in open('i/10').readlines()),
          [0]
        )
      )
    ][20::40]
  )
)


# def f(l):
#   global X;
#   if 'a' in l:o=[X,X];X+=int(l[4:]); return o
#   return [X]