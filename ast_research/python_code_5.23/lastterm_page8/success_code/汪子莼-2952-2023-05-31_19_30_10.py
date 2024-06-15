def print_matrix(n):
    for x in range(n):
        for y in range(n):
            print(min(x,y)+1,end=" ")
        print()
           

number=eval(input())
print_matrix(number)



