def print_matrix(n):
    for i in range(n):
            print("")
            for x in range(n):
                if i <x:
                    print(i+1,end=" ")
                else:
                    print(x+1,end=" ")
    
                  

number=eval(input())
print_matrix(number)



