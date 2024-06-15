list1=eval(input())
list1.sort(reverse=True)
sum=''
for i in range(len(list1)):
    sum=sum+str(list1[i])
print(int(sum))



