n,m,l=map(int, input().split(','))
array=[n]
for i in range(n-1):
    n=n+l
    array.append(n)
print(array)
