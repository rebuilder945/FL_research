def print_matrix(n):
    for i in range(1,n+1):
         a = ""
         for x in range(1,i+1):
               b = str(x)+" "
               a = a+b
         d = str(i)+" "
         e = a + d*(n-i)
         e = e.rstrip()
         print(e)
    
       
         

number=eval(input())
print_matrix(number)



