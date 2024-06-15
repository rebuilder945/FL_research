def print_matrix(n):
    for i in range(1,n+1):
        row=" ".join(str(min(i,j)) for j in range(1,n+1))
        print(row)
    
        

number=eval(input())
print_matrix(number)



