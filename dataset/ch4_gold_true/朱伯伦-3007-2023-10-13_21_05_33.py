list1=eval(input())
n,m=eval(input())
list2=[]
if n>m or m>len(list1):
    print("error")
else:
    list3=list1[n:m]
    for x in list1:
        if x not in list3:
            list2.append(x)
        else:
            continue
    print(list2)
        
