a=eval(input())
lst=[i+1 for i in range(a)]
for i in range(a-1):
    lst[i]=lst[i+1]
lst[a-1]=1
print(lst)
