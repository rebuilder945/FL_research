n,m,l=map(int,input().spilt(","))
array=[n]
for i in range(m-l):
    n=n+l
    array.append(n)
print(array)

