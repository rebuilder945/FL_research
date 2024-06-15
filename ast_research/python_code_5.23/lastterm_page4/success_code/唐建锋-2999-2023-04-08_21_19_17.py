a=input().split()
b=input().split()
m,n=int(b[0]),int(b[1])
lst=[a]
lst[m][n]=lst[n][m]
print(lst)

