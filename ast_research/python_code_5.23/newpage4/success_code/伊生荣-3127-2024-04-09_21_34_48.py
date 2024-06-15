n=int(input())
lst = [i for i in range (1,n+1)]
temp = 1
for i in range(1,n):
    lst[i-1]=lst[i]
lst[n-1]=temp
print(lst)
