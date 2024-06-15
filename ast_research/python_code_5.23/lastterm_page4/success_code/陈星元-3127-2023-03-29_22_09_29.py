n=eval(input())
list=[x for x in range(1,n+1)]
for x in list:
    if list.index(x)==0:
        A1=x
    else:
        m=list.index(x)
        list[m-1]=list[m]
list[-1]=A1
print(list)



