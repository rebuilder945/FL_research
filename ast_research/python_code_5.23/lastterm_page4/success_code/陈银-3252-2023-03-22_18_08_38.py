def Fibonacci(num,n):
    a = num[0];
    b = num[1];
    end = 1;
    for x in range(n):
        if x < 2:
            end = 1
        else:
            end  = a + b
            a = b
            b = end 
    return end





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


