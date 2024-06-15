def print_matrix(n):
    s=[1]*n
    for x in range(1,n):
        print(" ".join(map(str,s)))   
        s[x:]=[x+1]*(n-x)

number=eval(input())
print_matrix(number)



