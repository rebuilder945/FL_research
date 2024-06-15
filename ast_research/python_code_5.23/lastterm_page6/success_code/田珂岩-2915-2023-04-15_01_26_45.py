def shuixianhuashu(x):
    a = x // 100
    b = (x - a*100) // 10
    c = (x - a*100 - b*10)
    for i in range(100,x):
        if x == pow(a,3) + pow(b,3) + pow(c,3):
            return True
    return False
n = eval(input())
flag = 0
for i in range(100,n+1):
    if shuixianhuashu(i):
        flag = 1
        print(i)
if flag == 0:
    print("none")            

