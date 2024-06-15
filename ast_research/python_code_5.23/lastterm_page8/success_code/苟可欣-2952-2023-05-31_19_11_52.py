def print_matrix(n):
    
    for x in range(1,n+1):
        a=0
        for k in range(1,x):
            print(k,end=" ")
            a=a+1
        for i in range(n):
            print(x,end=" ")
            a=a+1
            if a==n:
                print(" ")

number=eval(input())
print_matrix(number)



