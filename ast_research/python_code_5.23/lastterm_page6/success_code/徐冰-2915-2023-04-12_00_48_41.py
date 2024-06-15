def shuixianhua(x):
    ls=list(map(int,list(str(x))))
    ls1=[]
    for i in ls:
        ls1.append(i**3)
    if x==sum(ls1):
        return True
    else:
        return False
n=eval(input())
ls2=[]
for x in range(100,n+1):
    if shuixianhua(x):
        ls2.append(x)
if ls2==[]:
    print("none")
else:
    for x in ls2:
        print(x)
