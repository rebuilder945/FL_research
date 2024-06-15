s=input()
temp=['No digits']
for i in range(len(s)):#遍历每个元素
    sub=[]
    while i<len(s) and s[i].isdigit():#元素为数字时加入
        sub.append(s[i])
        i+=1
    if len(sub)>=len(temp):
        temp=sub
print(''.join(temp))
