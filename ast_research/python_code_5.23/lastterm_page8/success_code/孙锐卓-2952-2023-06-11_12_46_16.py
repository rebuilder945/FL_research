def print_matrix(n):
    for i in range(n):
        line=[]
        for j in range(n):
            if j +1<=i+1:
                line.append(str(i+1))
        print(' '.join(line))

number=eval(input())
print_matrix(number)



