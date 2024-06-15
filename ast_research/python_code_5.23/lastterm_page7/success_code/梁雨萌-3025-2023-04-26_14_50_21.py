word=input().split()
word.sort()
dic={}
for i in word:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
max=0
for i in dic:
    if dic[i]>=max:
        max=dic[i]
for i in dic:
    if dic[i]==max:
        print(i,dic[i])
    

