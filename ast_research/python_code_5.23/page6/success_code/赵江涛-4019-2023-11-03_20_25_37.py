a = eval(input())
while a+1>0:
    s = 1
    g=a%10+5
    g=g%10
    a=int(a//10)
    s = (s-1)*10+g
print(s)
    

    
