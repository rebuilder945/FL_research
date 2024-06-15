n=eval(input())
list=[i for i in range(1,n+1)]
for i in range(1,n):
    list[i-1]=list[i]
list[-1]=1
print(list)
    
