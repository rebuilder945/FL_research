def print_matrix(n):
    for i in range(1,n+1):
          for x in range(1,n+1):
                if x>i:
                   x=str(x)+" "
                   print(x)
                else:
                   i=str(i)+" "
                   print(i)

number=eval(input())
print_matrix(number)



