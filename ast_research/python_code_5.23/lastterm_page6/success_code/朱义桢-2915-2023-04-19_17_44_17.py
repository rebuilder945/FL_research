def shuixianhua(a):
    a=str(a)
    b=0
    for x in a[:]:
        b+=int(x)**len(a)
    if b==int(a):
        return True
a=eval(input())
m=[]
for x in range(1,a+1):
    if shuixianhua(x):
        m.append(x)
for x in m:
    print(x)
