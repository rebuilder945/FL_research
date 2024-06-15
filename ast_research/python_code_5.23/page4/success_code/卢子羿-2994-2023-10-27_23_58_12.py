x=eval(input())
list1=list(x)
n,m=eval(input())
a=list1[n]
if a<=len(list1):
    list2=[]
    list2.append(a)
    list3=list2*m
    list4=list1+list3
    print(list4)
else:
    print("error")


