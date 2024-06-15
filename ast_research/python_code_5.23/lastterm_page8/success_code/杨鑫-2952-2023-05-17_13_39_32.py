def print_matrix(n):
    for x in range(1,n+1):
        i = 0
        for y in range(1,x+1):
            print(y,end=" ")
            i+=1
        while i < n:
            print(x,end=" ")
            i+=1
        print()

number=eval(input())
print_matrix(number)



