def print_matrix(n):
    num=1
    while num<n+1:
        ls=[num]*n
        i=0
        while i+1<num:
            ls[i]=i+1
            i=i+1
        ls1=[str(m) for m in ls]
        print(" ".join(ls1))
        num=num+1

number=eval(input())
print_matrix(number)



