def shuixianhua(x):
    a=[i for i in str(x)[:]]
    a=list(map(int,a))
    if a[0]**3+a[1]**3+a[2]**3==x:
        return True
    else:
        return False
n=eval(input())
b=[]
for x in range(100,n+1):
    if shuixianhua(x):
        b.append(x)
if b==[]:
    print("none")
else:
    for x in b:
        print(x)
