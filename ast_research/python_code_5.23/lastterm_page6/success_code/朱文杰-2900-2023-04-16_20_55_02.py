def P(x):
    for i in range(2,x+1):
        if i>2:
            for j in range(2,i):
                if i%j==0:
                    return False
                else:
                    return True
    x=eval(input())
def Q(x):
    x=eval(input())
    str1=str(x)[::-1]
    if str1==str(x):
        return True
    else:
        return False
x=eval(input())
m=[]
for i in range(2,x+1):
    if  P(x)==True and Q(x)==True:
        m.append(i)
        print(" ".join(m))
    else:
        print("illegal input")
