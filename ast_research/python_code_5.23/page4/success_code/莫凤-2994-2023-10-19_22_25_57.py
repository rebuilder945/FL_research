a=eval(input())
list1=list(a)
a,b=eval(input())
if 0<=a<len(list1):
    c=list1[a]
    for x in range(b):
        list1.append(c)
    print(list1)
elif -len(list1)<=a<0:
    c=list1[a]
    for x in range(b):
        list1.append(c)
else:
    print("error")
