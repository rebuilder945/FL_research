n = eval(input())
list1= [i for i in range(1,n+1)]
temp=list1[0]
for i in range(0,len(list1)-1):
    list[i]=list[i+1]
list[-1]=temp
print(list1)
