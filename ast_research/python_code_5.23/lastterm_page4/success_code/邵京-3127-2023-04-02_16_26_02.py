n=eval(input())
numbers=[x for x in range(1,n+1,1)]
for i in range(0,len(numbers)):
    if i<n-1:
        numbers[i]=numbers[i+1]
    elif i==n-1:
        numbers[i]=1
print(numbers)
