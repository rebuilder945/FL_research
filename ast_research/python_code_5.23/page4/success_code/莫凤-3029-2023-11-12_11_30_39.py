a=input().split(",")
b=eval(input())
list1=[]
for x in range(len(a)):
    list2=[]
    list2.append(a[x])
    list2.append(b[x])
    list1.append(list2)
print(list1)
