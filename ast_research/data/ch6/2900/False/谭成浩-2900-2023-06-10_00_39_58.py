def zhishu(m):
    if m==1:
        return 0
    elif m==2:
        return 1
    else:
        for i in range(2,m):
            if m%i==0:
                return 0
            elif i==m-1 and m%i>0:
                return 1
            else:
                continue
def huiwenshu(m):
    m=str(m)
    j=0
    for i in range(len(m)//2):
        if m[i]==m[-(i+1)]:
            j=1
        else:
            j=0
            break
    return j
n=eval(input())
if n<0 or type(n)==float:
    print("illegal input")
else:
    x=[2,3,5,7]
    for i in range(n+1):
        if zhishu(i)==1 and huiwenshu(i)==1:
            x.append(i)
        else:
            continue
    for i in x:
        print(i,end=' ')
