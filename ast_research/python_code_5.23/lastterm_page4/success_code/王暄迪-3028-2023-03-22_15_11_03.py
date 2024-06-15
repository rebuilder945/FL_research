a=list(input().split(","))
b=int(a[0])
c=int(a[1])
d=int(a[2])
list1=[b]
for i in range(c-1):
    b+=d
    list1.append(b)
print(list1)
