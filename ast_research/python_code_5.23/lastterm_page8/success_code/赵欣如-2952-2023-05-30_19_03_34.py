def print_matrix(n):
    a=1
    while a<=n:
        b=[str(x) for x in range(1,a+1)]
        c=[str(a)]*(int(n)-int(a))
        ls=b+c
        a+=1
        d=" ".join(ls)
        print(d)

number=eval(input())
print_matrix(number)



