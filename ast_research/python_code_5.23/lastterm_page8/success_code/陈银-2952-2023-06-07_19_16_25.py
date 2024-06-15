def print_matrix(n):
    for x in range(n):
        for y in range(n):
            if y>x:
                print(x,end=" ")
            else:
                print(y,end=" ")
            print()

number=eval(input())
print_matrix(number)



