def Fibonacci(temp):
Sum = 0  
num2 = 1  
num1 = 1  
if n == 1 or n == 2:  
    num2 = 1
    Sum = n  
else:
    Sum = 2
    for a in range(0, n - 2):  
        temp2 = num2  
        temp1 = num1  
        temp = temp1 + temp2  
        Sum = Sum + temp  

        
        num2 = num1  
        num1 = temp  
return str(temp)  




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


