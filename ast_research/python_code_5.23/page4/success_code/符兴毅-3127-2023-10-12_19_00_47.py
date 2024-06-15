n = eval(input())
lis = [i for i in range(1,(n+1))]
# print(lis)
for index in range(n):
    if index!=(n-1):
        lis[index] += 1
    else:
        lis[index] = 1
print(lis)
