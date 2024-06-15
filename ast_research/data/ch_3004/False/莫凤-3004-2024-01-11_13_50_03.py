a=eval(input())
list1=[]
for x in a:
    if x==1 or x==2:
        list1.append(x)
    else:
        for y in range(2,x):
            if x%y==0:
                break
        else:
            list1.append(x)
print(list1)
