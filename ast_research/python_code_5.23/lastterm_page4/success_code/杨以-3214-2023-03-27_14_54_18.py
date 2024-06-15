list=eval(input())
a=list.count(0)
b=a
while a>0:
    a-=1
    list.remove(0)
while b>0:
    b-=1
    list.append(0)
print(list)



