list1=eval(input())
a=len(list1)
while 0 in list1:
    list1.remove(0)
while len(list1)<a:
    list1.append(0)
print(list1)
