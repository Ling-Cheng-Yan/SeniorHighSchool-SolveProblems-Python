import datetime
try:
    while True :
        a = input()
        b = a.split()
        c = input()
        d = c.split()
        d1=datetime.datetime(int(b[0]),int(b[1]),int(b[2]))
        d2=datetime.datetime(int(d[0]),int(d[1]),int(d[2]))
        print(abs((d1-d2).days))

except EOFError:
    pass