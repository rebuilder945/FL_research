a=input()
dic={}
while a!="q":
    if a in dic.keys():
        dic[a]+=1
    else:
        dic[a]=1
    a=input()
b=max(dic.valus())
for i in dic:
    if dic[i]==b:
        print(i,b)
        break
