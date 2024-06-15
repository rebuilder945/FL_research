def sushu(x):
    for x in list2:
        for i in range(2,x):
            if x%i==0:
                return False
list2=[]
list1=eval(input())
for i in list1:
    if sushu!=False:list2.append(i)
print(list2)   
