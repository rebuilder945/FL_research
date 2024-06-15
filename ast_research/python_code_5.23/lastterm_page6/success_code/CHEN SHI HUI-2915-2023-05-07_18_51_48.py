def cals(x):
    a=x%10
    b=x//10%10
    c=x//100
    if int(c)**3+int(b)**3+int(a)**3==x:
        return True
    else:
        return False


n=input()
l=[]
num=0
for i in range(100,1000):
    if cals(i):
        print(i)
        num+=1
if num==0:
    print('none')

