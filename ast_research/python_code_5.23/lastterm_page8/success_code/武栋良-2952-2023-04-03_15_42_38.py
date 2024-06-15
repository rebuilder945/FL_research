def print_matrix(n):
    c = ""
    for i in range(1,n+1):
         for x in range(1,i+1):
               b = str(x)
               c = c+b
         a = ""+c
         d = str(i)
         e = a +d*(n-i)
         print("{}".format(e,end =" "))
    
       
         

number=eval(input())
print_matrix(number)



