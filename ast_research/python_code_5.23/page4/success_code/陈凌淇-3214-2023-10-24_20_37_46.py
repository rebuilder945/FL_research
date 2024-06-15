list1=eval(input())
jishu=0
for i in range(len(list1)):
    if list1[i]!=0:
        list1[jishu]=list1[i]
        jishu+=1
for j in range(jishu,len(list1)):
    list1[j]=0
print(list1)
