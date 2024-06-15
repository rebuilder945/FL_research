def print_matrix(n):
    for x in range(1,n+1):
        a=[]
        for i in range(1,n+1):
            if i<x:
                a.append(i)
            else:
                a.append(x)
        for i in a:
            print(i,end=" ")
        print()

number=eval(input())
print_matrix(number)



