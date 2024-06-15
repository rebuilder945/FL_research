n=eval(input())
list1=[i for i in range(1,n+1)]
c=[1]
for i in range(0,len(list1)-1):
    list1[i]=list1[i+1]
print(list1+c)
