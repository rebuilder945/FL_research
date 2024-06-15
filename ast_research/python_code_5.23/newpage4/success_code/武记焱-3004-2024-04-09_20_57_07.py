list1=eval(input())
list2=[]
for x in list1:
    yes=1
    for i in range(2,):
        if x % i==0:
            yes=0
            list2.append(x)
        else:
            pass
print(list2)
