'''
輸入說明
一筆測試資料一行，包含許許多多但總數不超過 1000 個的大小寫英文字母和標點符號。
不可思議的是，裡面不會有任何空白字元。
輸出說明
如果重新安排順序後，有辦法讓這一堆英文字母變成迴文的話，輸出「yes !」，否則輸出「no...」。
注意，大寫和小寫字母視為相同，即 A 和 a 是一樣的，並且，請忽視所有非英文字母的字元。
範例輸入
ababa
bbaaa
Level
aaabbbcc
abcdefg
HowAreYouToday
A_man,_a_plan,_a_canal:_Panama.
範例輸出
yes !
yes !
yes !
no...
no...
no...
yes !
'''
#AC 
import sys
for x in sys.stdin: #x是每次讀入的字串
  i=0
  d={}
  count=[]
  key=[]
  odd=0
  even=0
  for e in range(26): #加26個0
    count.append(0)
  for e in range(26): #加26個字母序0~25
    key.append(e)
  d = dict(zip(key, count)) #兩個list合併成一個字典

  while (i<len(x)):
    if x[i].isalpha(): 
     d[ord(x[i].upper())-ord('A')]+=1   #計算讀到的「該字母」個數
    i+=1  
  for i in range(26):
    if (d[i]%2==0):
      even+=1
    else:
      odd+=1
#  print(odd,even)
#迴文 abba 偶2奇0 abcba 偶2奇1  abccba偶3奇0  abctcba偶 3奇1 a偶0奇1 aa偶1奇0 
#不迴文 cd奇2   abc奇3
  if odd>1  :
    print("no...")
  else:
    print("yes !")