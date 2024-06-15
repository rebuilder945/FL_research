strs=input() or "q"
lis=[]
while strs!="q":
    lis.append(strs)
    strs=input() or "q"
dic={}
for i in lis:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
lis1=list(dic.items())
print(lis1)
lis1.sort(key=lambda x:x[1])
print(f"{lis1[0][0]} {lis1[0][1]}")
