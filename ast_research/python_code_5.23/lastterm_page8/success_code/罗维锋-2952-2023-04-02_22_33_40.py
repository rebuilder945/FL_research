def print_matrix(n):
    s=[1]*n
    for i in range(n):
        print(" ".join(map(str,s)))
        for x in range(1,n):
            s[x:]=[x+1]*(n-x)

number=eval(input())
print_matrix(number)



