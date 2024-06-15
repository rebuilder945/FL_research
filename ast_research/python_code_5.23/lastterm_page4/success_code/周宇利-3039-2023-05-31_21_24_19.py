list1=eval(input())
a=max(list1)
b=min(list1)
jishu1=0
jishu2=0
for i in list1:
    if i==a or i==b:
        list1[jishu2]='#'
        list1[jishu1]="#"
        jishu1+=1
        jishu2+=1
        while jishu1>0:
            list1.remove('#')
            jishu1-=1
print(list1)
