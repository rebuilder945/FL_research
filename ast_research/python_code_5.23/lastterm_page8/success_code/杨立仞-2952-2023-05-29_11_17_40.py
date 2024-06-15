def print_matrix(n):
    for i in range(n):
        for j in range(n):
            if i ==j:
                print(i,end="")
            elif i<j:
                print(i,end="")
            else:
                print(j,end="")
        print()

number=eval(input())
print_matrix(number)



