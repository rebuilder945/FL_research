list1=eval(input())
x=list1.count(i for i in list1)
while True:
    if x==1:
        break
    else:
       y=list1.index(i for i in list1)
       list1.pop(y)
       break
print(list1)
