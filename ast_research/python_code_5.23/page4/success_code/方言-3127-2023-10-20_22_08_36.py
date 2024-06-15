s=int (input())
list=[i for i in range(1,s+1)]
for i in range (s-1):
    list[i]=list[i+1]
list[-1]=1
print(list)

