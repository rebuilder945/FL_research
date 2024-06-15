def check(x):
    a,b,c=x%10,(x//10)%10,x//100
    if a**3+b**3+c**3==x:
        return True
    else:
        return False

num=eval(input())
flag=False
for x in range(100,min(num+1,1000)):
    if check(x):
        flag=True
        print(x)
if flag==False:
    print('none')
