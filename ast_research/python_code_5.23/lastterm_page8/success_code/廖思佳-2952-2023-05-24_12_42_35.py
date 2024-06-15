def print_matrix(n):
        for i in range(n):
            for j in range(n):
                if j>=i:
                    print(i+1,end=" ")
                else:
                    print(j+1,end=" ")    
            print("\n")
        return     

number=eval(input())
print_matrix(number)



