def print_matrix(n):
    for i in range(1,n+1):
          for x in range(1,n+1):
                if int(x)>=i:
                   x=x+" "
                   print(x)
                else:
                   i=i+" "
                   print(i)

number=eval(input())
print_matrix(number)



