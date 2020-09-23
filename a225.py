while True:
    try:
        m = input()
        n = list(map(int, input().split()))
        n.sort(reverse=True)
        n.sort(key = lambda x: x%10)
        
        print(" ".join([str(i) for i in n]))

    except:
        break
