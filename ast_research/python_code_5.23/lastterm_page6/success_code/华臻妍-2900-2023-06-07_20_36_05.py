
def a(x):
    flag=True#判断定义真假
    if x==2:
        return True
    for j in range(2,x):
        if x%j==0:
            flag=False
    if flag:
        return True

def b(x):
    temp=x
    sum=0
    while x>0:
        c=x%10
        sum=sum*10+c
        x=x//10
    if sum==temp:
        return True

n=eval(input())
if type(n) is int and n>1:
    for x in range(2,n):
        if a(x) and b(x):
            print(x,end=' ')
else:
    print("illegal input")
