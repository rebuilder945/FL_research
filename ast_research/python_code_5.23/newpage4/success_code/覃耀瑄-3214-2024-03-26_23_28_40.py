list1=eval(input())
m=len(list1)
while 0 in list1:
    list1.remove(0)
    n=len(list1)
while m>n:
    list1.append(0)
    n=len(list1)
print(list1)

