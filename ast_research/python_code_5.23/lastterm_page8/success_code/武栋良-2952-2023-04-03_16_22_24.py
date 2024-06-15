def print_matrix(n):
    for i in range(1,n+1):
         a = ""
         for x in range(1,i+1):
               b = str(x)+" "
               a = a+b
         c = str(i)+" "
         d = a + d*(n-i)
         d = d.rstrip()
         print(d)
    
       
         

number=eval(input())
print_matrix(number)



