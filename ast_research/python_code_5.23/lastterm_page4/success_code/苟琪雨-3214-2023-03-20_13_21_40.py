list1=eval(input())
a=list1.count(0)
while list1.count(0)>=1:
    list1.remove(0)
for i in range(a):
    list1.append(0)
print(list1)
