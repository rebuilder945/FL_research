def print_matrix(n):
    for x in range(n):
            for y in range(n):
                if y<x and y<n-1:
                    print(y+1,end=' ')
                elif y>=x and y<n-1:
                    print(x+1,end=' ')
                else:
                    print(x+1)

number=eval(input())
print_matrix(number)



