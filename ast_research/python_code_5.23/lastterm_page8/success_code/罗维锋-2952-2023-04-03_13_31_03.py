def print_matrix(n):
    s=[1]*n
    print(" ".join(map(str,s)))
    for x in range(1,n):   
        s[x:]=[x+1]*(n-x)
        print(" ".join(map(str,s)))

number=eval(input())
print_matrix(number)



