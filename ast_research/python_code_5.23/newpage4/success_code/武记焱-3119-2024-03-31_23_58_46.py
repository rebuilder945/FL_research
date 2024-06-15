list1=eval(input())
x=list1.count(i for i in list1)
while True:
    if x==1:
        break
    else:
        list1.remove(i for i in list1)
print(list1)
