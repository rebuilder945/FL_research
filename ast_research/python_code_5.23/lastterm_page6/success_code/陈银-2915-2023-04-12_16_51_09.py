def shuixian(i):
    a = i//100
    b = (i-100*a)//10
    c = i-(100*a+10*b)
    if a**3+b**3+c**3==i:
        return True
i = eval(input())
for x in range(100,i):
    if shuixian(x):
        print(x)
    
