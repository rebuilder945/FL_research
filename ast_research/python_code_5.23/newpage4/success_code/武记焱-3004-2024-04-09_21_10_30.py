list1=eval(input())
list2=[]
for x in list1:
    if x==0 or x==1:
        pass
    else:
        yes=1
        for i in range(2,):
            if i>0:
                x % i==0
                yes=0
                list2.append(x)
            elif i==0:
                pass
            else:
                pass
print(list2)
