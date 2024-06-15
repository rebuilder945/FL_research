def print_matrix(n):
    s=[1]*n
    a=[s]
    for x in range(1,n):
        s[x:]=[x+1]*(n-x)
        a.append(s)
    for i in range(n):
        print(" ".join(map(str,a[i])))

number=eval(input())
print_matrix(number)



