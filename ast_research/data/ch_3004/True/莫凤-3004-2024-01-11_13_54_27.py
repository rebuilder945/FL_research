a=eval(input())
list1=[]
for x in a:
    if x==2:
        list1.append(x)
    elif x>2:
        for y in range(2,x):
            if x%y==0:
                break
        else:
            list1.append(x)
print(list1)
