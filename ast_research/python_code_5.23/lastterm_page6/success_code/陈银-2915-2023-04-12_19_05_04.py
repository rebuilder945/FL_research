def shuixian(i):
    a = i//100
    b = (i-100*a)//10
    c = i-(100*a+10*b)
    if a**3+b**3+c**3==i:
        return True
i = eval(input())
c = []
if i<1000:
    for x in range(100,i+1):
        if shuixian(x):
            c.append(x)
            print(x)
elif i>=1000:
    for x in range(100,1000):
        if shuixian(x):
            c.append(x)
            print(x)
if len(c)==0:
    print("none")
  


