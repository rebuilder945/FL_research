def print_matrix(n):
    s=[1]*n
    a=[s]
    for x in range(2,n+1):
        s[x:]=[x]*(n-x+1)
        a.append(s)
    for i in range(n):
        print(" ".join(map(str,a[i])))

number=eval(input())
print_matrix(number)



