list1=eval(input())
list2=[]
list3=[]
for i in list1:
    if i==1:
        list3.append(i)
    elif i==2:
        pass
    else:
        for m in range(2,i):
            if i%m==0:
                list3.append(i)
for i in list1:
    if i in list1 and i not in list3:#两个i记住了！11！！111！！1！！！111
        list2.append(i)
print(list2)

