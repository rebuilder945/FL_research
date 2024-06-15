list1=eval(input())
num=[]
for i in range(0,len(list1)):
    for j in range(2,list1[i]):
        if(list1[i]%j==0):
            break
    else:
        num.append(list1[i])
print(num)
