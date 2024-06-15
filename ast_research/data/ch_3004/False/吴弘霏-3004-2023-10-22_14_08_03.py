list=eval(input())
list1=[]
for i in list:
    if i>=2:
        for j in range(2,i):
            if i%j==0:
                break
        list1.append(i)
print(list1)
