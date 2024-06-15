list1=eval(input())
x=0
for i in range(len(list1)):
    for j in list1:
        if j==list1[i]:
            x=x+1
    if x != 1:
        for k in range(x-1):
            list1.remove(list1[i])
    else:
        break
print(list1)
    

