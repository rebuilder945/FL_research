def shuixianhua(a):
    a=str(a)
    b=0
    for x in a[:]:
        b+=int(x)**3
    if b==int(a):
        return True
a=eval(input())
m=[]
for x in range(100,a+1):
    if shuixianhua(x):
        m.append(x)
if m==[]:
    print("none")
else:
    for x in m:
        print(x)
