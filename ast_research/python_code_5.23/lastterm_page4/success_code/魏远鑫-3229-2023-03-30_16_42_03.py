list=eval(input())
li=[]
for i in list:
    if list.count(i)==1:
        li.append(i)
        li.sort()
        separator=','
        result=separator.join(str(i) for i in li)
print(result)


