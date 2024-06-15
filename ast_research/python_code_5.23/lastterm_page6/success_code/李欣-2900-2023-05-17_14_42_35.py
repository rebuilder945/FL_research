def sushu(x):    
    if x<=1:
        return False
    for i in range(2,int(x**0.5+1)):
        if x%i==0:
            return False
        return True
def huiwen(y):
    sty=str(y)
    if sty==sty[::-1]:
        return y
n=input()
if int(n)<=1 or str(n).count('.')==1:
    print("illegal input")
else:
    b=[]
    for m in range(2,int(n+1)):
        if sushu(int(m)) and huiwen(int(m)) and m%3!=0:
            b.append(str(m))
    print(" ".join(b))
