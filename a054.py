while True:
  try:
    a=input()
    k=0
    b=[1,10,19,28,37,46,55,54,39,73,82,2,11,20,48,29,38,47,56,65,74,83,21,3,12,30]
    c=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(0,8,1):
      k=k+int(a[i])*(8-i)

    for l in range(26):
      if((k+int(b[l])+int(a[8]))%10==0):
        print(c[l],end="")
    print()
  
  except:
    break