def sushu(x):    
    for i in range(2,int(x**0.5+1)):
        if x%i!=0:
            return True
        else:
            return False
def huiwen(y):
    sty=str(y)
    if sty==sty[::-1]:
        return y
n=200
b=[]
if int(n)>3:
    b.append(str(2))
    b.append(str(3))
elif int(n)==3 or int(n)==2:
    b.append(str(2))
if str(n).count('.')==1 or float(n)<=1:
    print("illegal input")
else:
    for m in range(2,int(n+1)):
        if sushu(m) and huiwen(m):
            b.append(str(m))
    print(" ".join(b))
