list1=eval(input())
x=list1.count(i for i in list1)
if x==1:
    pass
elif x>1:
    while x==1:
        list1.remove(i for i in list1)
        break
print(list1)
