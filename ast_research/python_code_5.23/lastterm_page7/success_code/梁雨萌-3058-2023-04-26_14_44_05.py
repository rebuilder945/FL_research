list=[]
while True:
    word=input()
    if word!="q":
        list.append(word)
    else:
        break
dic={}
for i in list:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]=dic[i]+1
max=0
word=""
for i in dic:
    if dic[i]>=max:
        max=dic[i]
        word=i
print(word,max)


