a=eval(input())
list1=list(range(1,a+1))
jishu=0
n=0
for x in list1:
    if jishu==0:
        n=x
        list1[jishu]=list1[jishu+1]
        jishu+=1
    elif jishu==len(list1)-1:
        break
    else:
        list1[jishu]=list1[jishu+1]
        jishu+=1

print(list1)
