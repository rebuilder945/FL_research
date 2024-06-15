def print_matrix(n):
        if n ==1:
              print(1)
        else:
             for x in range(1,n+1):
                  num=1
                  c=0
                  for y in range(1,n+1):
                        c+=1
                        if num< x:
                            print(num,end=" ")
                            num+=1
                        else:
                            print(num,end=" ")
                        if c==n:
                            print()

number=eval(input())
print_matrix(number)



