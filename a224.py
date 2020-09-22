import re
while True :
    try :    
        a = input()
        temp = 0
        flag = False
        a = a.lower().strip()
        a = re.sub("[^a-zA-Z]+", "", a)
        if (len(a) / 2) == (len(a) // 2) :
            for i in range(len(a)) :
                if a[i] != a[len(a) - 1 - i] :
                    print("no...")
                    flag = True
                    break
            if flag is False :
                print("yes !")
        else :
            temp = len(a) // 2
            for i in range(temp) :
                if a[i] != a[len(a) - 1 - i] :
                    print("no...")
                    flag = True
                    break
            if flag is False :
                print("yes !")
    except :
        break








