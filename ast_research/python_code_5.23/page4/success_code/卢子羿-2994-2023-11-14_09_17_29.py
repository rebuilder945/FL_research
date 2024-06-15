x=eval(input())
list1=list(x)
n,m=eval(input())
if n+1<=len(list1):
    list2=[]
    list2.append(list1[n])
    list3=list2*m
    list4=list1+list3
    print(list4)
else:
    print("error")

