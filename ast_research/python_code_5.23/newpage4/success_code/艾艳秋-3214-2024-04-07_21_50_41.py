list1=eval(input())
list1.sort()
x=list1.count(0)
y=list1[0:x]
z=list1[x:]
m=z+y
print(m)
