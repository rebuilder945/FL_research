a=input().split(",")
b=input().strip("[]").split(",")
list1=[]
for x in range(len(a)):
    list2=[]
    list2.append(a[x])
    list2.append(b[x])
    list1.append(list2)
print(list1)
