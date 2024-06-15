def f(x):
    jishu=0
    if x==1 or x==0:
        return -1
    for x1 in range(2,x):
        if x%x1==0:
            jishu+=1
    return jishu
list1=eval(input())
list2=[]
for x in list1:
    b=f(x)
    if b==0:
        list2.append(x)
print(list2)
