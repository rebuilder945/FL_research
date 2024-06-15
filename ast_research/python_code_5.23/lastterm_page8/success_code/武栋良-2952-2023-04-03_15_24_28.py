def print_matrix(n):
    for i in range(1,n+1):
         b = str(i)
         a = ""+b
         a = a +b*(n-i)
         print({}.format(a,end =" "))
    
       
         

number=eval(input())
print_matrix(number)



