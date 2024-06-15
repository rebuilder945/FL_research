n=eval(input())
def sushu(y):
    x=[]
    for i in range(y):
        if i>=2:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                x.append(i)
    return set(x)
def huiwen(z):
    m=[]
    for x in range(z):
        p=str(x)
        q=p[::-1]
        if p==q:
            m.append(x)
    return set(m)
number=sushu(n)&huiwen(n)
number=list(number)
for i in number:
    print(i,end=" ")


