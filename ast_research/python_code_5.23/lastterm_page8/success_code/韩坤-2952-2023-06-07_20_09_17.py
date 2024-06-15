def print_matrix(n):
    for x in range(1,n+1):
        if x==1:
            lst=[1]*n
            print(*lst,end="")
            print("\n")
        else:
            lst=[y for y in range(1,x)]
            lst1=[x]*(n+1-x)
            lst.extend(lst1)
            print(*lst,end="")
            print("\n")
            

number=eval(input())
print_matrix(number)



