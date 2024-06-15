a=input().split(",")
b=eval(input())
list2=[]
for x in list(range(len(a))):
    c=[a[x],b[x]]
    list2.append(c)
print(list2)

