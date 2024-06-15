a = eval(input())
while a>0:
    s = 0
    g=a%10+5
    g=g%10
    s = 10*s+g
    a = a//10
print(s)
    
