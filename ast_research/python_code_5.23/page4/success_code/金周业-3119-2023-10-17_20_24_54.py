list1=eval(input())
x=0
for i in list1:
    for j in list1:
        if i==j:
            x=x+1
    if x != 0:
        for i in range(x-1):
            list1.remove(i)
    else:
        break
print(list1)
    

