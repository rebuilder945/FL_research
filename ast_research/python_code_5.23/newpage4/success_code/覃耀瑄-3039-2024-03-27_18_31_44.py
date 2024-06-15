list1=eval(input())
list1.sort()
x=max(list1)
m=min(list1)
while x in list1:
        list1.remove(x)
while m in list1:

        list1.remove(m)
print(list1)

