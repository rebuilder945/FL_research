list = eval(input())
list1=[]
for i in list:
    if i>=2:
        for x in range(2,i):
            if i%x==0:
                break
        else:
            list1.append(i)
print(list1)


