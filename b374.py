import re

s = input("")
s = s.strip(" \t\r\n")
n = int(s)

s = input("")
s = s.strip(" \t\r\n")
s = s.split()

c = {}
for i in s:
    a = int(i)

    if a in c:
        c[a] += 1
    else:
        c[a] = 1
        
max_count = 0
for i in c:
    if c[i] > max_count:
        max_count = c[i]

for i in sorted(c.keys()):
    if c[i] == max_count:
        print("{0} {1}".format(i, max_count))