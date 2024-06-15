def print_matrix(n):
    for x in range(n):
        for y in range(n):
            if y<=x :
                print(y,end=" ")
            else:
                print(x,end=" ")
        print()

number=eval(input())
print_matrix(number)



