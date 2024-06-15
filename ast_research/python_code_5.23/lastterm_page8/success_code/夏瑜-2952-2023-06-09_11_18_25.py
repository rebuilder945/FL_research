def print_matrix(n):
        for i in range(n):
            for j in range(n):
                if i>j:
                    print(j,end=" ")
                else:
                    print(i,end=" ")
            print()


number=eval(input())
print_matrix(number)



