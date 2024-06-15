dic={}
while True:
    s=input()
    if s=="q":
        break
    elif s in dic:
        dic[s]+=1
    else:
        dic[s]=1
max=0
maxword=''
for word,count in dic.items():
    if count>max:
        max=count
        maxword=word
print(maxword,max)
