def print_matrix(n):
    str = ""
    for i in range(1,n+1):
     str +=str(i)
    pointer = 1
    for j in range(1,n+1):
     var = str[:poinyer]+str(j)*(n-1)
     pointer+=1
     n-=1
     for i in var:
      print(int(i),end="\t")
     print("\n")

number=eval(input())
print_matrix(number)



