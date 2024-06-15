def print_matrix(n):
    for i in range(1,n+1):
        ls=[x for x in range(1,i+1)]
        if n==1:
            print(1)
        else:
            for p in ls:
                print(p,end=" ")
            if n-len(ls)-1>0:
                for q in range(n-len(ls)-1):
                    print(ls[-1],end=" ")
                print(ls[-1])
            elif n-len(ls)-1=0:
                print(ls[-1])
            else:
                pass


number=eval(input())
print_matrix(number)



