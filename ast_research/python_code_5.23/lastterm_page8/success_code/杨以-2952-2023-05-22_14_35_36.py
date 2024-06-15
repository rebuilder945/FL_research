def print_matrix(n):
    for i in range(int(n)):
        for j in range(int(n)):
            if i<j:
                print(i+1,end=' ')
            elif i>=j:
                print(j+1,end=' ')
        print('')

number=eval(input())
print_matrix(number)



