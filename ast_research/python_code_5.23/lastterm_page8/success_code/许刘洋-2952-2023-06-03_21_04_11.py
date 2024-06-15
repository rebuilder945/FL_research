def print_matrix(n):
    print('\n'.join(' '.join([str(min(x,y))for x in range(1,n+1)])for y in range(1,n+1)))

number=eval(input())
print_matrix(number)



