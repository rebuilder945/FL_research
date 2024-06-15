def print_matrix(n):
    num = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if num < i:
                print(num,end=" ")
                num=num+1
            else:
                print(num,end=" ")
            print("\n")

number=eval(input())
print_matrix(number)



