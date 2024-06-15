list1=eval(input())
list2=[]
for x in list1:
    yes=1
    for i in range(2,):
        if x>0:
            x % i==0
            yes=0
            list2.append(x)
        elif x==0:
            pass
        else:
            pass
print(list2)
