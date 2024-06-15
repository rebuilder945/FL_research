dic={}
a=True
while a:
    b=input()
    if b=='q':
        break
    else:
        if b in dic:
            dic[b]+=1
        else:
            dic[b]=1
m=max(dic.keys(),key=(lambda x:dic[x]))
print(m,dic[m])
