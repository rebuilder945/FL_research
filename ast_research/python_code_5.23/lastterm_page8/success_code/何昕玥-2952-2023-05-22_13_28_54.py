def print_matrix(n):
    for i in range(n):
         for j in range(1,n+1):
              if i<=j:
                 print(i,end=" ")
              else:
                 print(j,end=" ")
         print("\n")

number=eval(input())
print_matrix(number)



