lis=eval(input())
str1=""
dic={}
for i in lis:
    str1+=i
for i in str1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
dic.sort(dic.items,key=lambda x:x[0])
for i in dic:
    print(f"{i},{dic[i]}")
