def print_matrix(n):
    def  print_matrix(n):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if j % n!= 1:
                    print ("{:<2}". format (min(i,j)), end ="") 
                else :
                    print()
                    print ("{:<2}". format (min(i,j)), end ="")       


number=eval(input())
print_matrix(number)



