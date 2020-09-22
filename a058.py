num1 = list()
a = 0
b = 0 
c = 0

num = int(input())
if 1 <= num and num <= 50000 :
    while num > 0 :
        d = input()
        num1.append(d)
        num = num - 1

for i in num1 :
    if int(i) % 3 == 0 :
        a = a + 1
    elif int(i) % 3 == 1 :
        b = b + 1
    elif int(i) % 3 == 2 :
        c = c + 1
    else :
        break

print(a, b, c)
   

