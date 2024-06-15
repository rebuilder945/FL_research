def print_matrix(n):
        for r in range(n):
            for c in range(n):
                output=min(r+1,c+1)
                print(output,end=" ")
            print("\n")

number=eval(input())
print_matrix(number)



