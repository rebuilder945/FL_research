def print_matrix(n):
    for i in range(1,n+1):
         for x in range(1,i+1):
               b = str(x)
               c = ""+b
         a = ""+c
         d = str(i)
         a = a +d*(n-i)
         print("{}".format(a,end =" "))
    
       
         

number=eval(input())
print_matrix(number)



