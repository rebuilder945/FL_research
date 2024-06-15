n = eval(input())
for x in range(100,n+1):
    s= str(x)
    a,b,c = s[0],s[1],s[2]
    sum = int(a)**3+int(b)**3+int(c)**3
if sum == x:
    print(x,end=' ')

