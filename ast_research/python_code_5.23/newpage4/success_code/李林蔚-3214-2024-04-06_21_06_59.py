list1=eval(input())
jishu1=0
jishu2=0
for x in list1:
    if x==0:
        list1[jishu2]='#'
        jishu1+=1
    jishu2+=1
while jishu1>0:
    list1.remove('#')
    list1.append(0)
    jishu1-=1
print(list1)
