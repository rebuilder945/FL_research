def f(x):
    jishu=0
    for x1 in range(2,x):
        if x%x1==0:
            jishu+=1
    if jishu==0:
        return 0
    elif jishu!=0:
        return 1
    elif x==0 or x==1:
        return 1
list1=eval(input())
list2=[]
for x in list1:
    if f(x)==0:
        list2.append(x)
print(list2)
