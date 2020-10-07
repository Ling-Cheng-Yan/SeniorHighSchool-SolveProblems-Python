import sys
for line in sys.stdin:
  A,b,C = line.split()
  a = int(A)
  c = int(C)
  if b == '+':
    d = a + c
  elif b == '-':
    d = a - c
  elif b == '*':
    d = a * c
  elif b == '/':
    d = a / c
  e = int(d)
  print(e)