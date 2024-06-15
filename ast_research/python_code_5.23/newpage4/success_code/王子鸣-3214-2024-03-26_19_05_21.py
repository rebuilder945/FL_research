list1=eval(input())
a=len(list1)
for i in range(a):
    if list1[i]!=0:
        i+=1
    else:
        del list1[i]
        list1.append(0)
print(list1)

