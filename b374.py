n = int(input())
num = input().split()
saved_sum = 0
for i in range(30000):
    sum1 = 0
    for k in range(n):
        if i == (int(num[k])):
        sum1 = sum1 + 1
    if sum1 > saved_sum:
        saved_sum = sum1
        saved_i = i
        saved_j = 0
    elif sum1 == saved_sum:
        saved_j = i  
print(saved_i, saved_sum) 
if saved_j > 0:
    print(saved_j, saved_sum)