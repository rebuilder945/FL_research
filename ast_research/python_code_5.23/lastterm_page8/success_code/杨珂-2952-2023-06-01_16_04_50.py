def print_matrix(n):
    for i in range(1,n+1):
        b=n+1
        for x in range(1,i+1):
            print("x",end=" ")
        for a in range(i+1,b):
            print("i",end=" ")
        print("\n")

number=eval(input())
print_matrix(number)



