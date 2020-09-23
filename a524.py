from itertools import permutations
try:
    while True:
        lst1 = list()
        lst2 = list()
        str1 = str()
        ans = int(input())
        ans = ans + 1
        for i in range(ans):
            lst1.append(i)
        del lst1[0]
        lst2 = list(permutations(lst1))
        print(lst2)
        length = len(lst2[0])
        for i in lst2:
            for j in range(length):
                for z in i:
                    str1 = str1 + str(z)
                print(str1)


except EOFError:
    pass

