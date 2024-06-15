def shuixian(x):
    x=str(x)
    s=0
    for i in x:
        a=int(i)**3
        s+=a
    if s==int(x):
        return True
    else:
        return False
n=eval(input())
ls=[]
for x in range(100,n+1):
    if shuixian(x):
        ls.append(x)
    else:
        continue
if len(ls)==0 or n<100:
    print("none")
else:
    for i in ls:
        print(i)
    

