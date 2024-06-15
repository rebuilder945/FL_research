list=eval(input())
list1=[]
for i in range(len(list)):
    for x in range(2,x):
        if i==2:
            list1.append(i)
        elif i>2 and i%x!=0:
            list1.append(i)
print(list1)
