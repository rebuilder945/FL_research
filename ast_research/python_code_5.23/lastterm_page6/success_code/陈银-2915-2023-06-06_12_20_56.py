def shuixianhua(m):
    a = m//100
    b = (m-100*a)//10
    c = m-100*a-10*b
    if m == a**3+b**3+c**3:
        return True
n = eval(input())
if n<153 :
    print("none")
elif n<1000:
    for x in range(100,n+1):
        if shuixianhua(x):
            print(x)
elif n >=1000:
    for x in range(100,1000):
        if shuixianhua(x):
            print(x)
