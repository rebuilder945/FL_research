k=input().split(' ')
n=int(k[0])
m=int(k[1])
lst=[]
if n>m or m-n<=2 or m<0 or n>=10 or m>=10:
    print('illegal input')
else:
    for i in range(n,m):
        num1=i
        for v in range(n,m):
            if str(v) not in str(num1):
                num2=num1*10+v
                for w in range(n,m):
                    if str(w) not in str(num2):
                        num3=num2*10+w
                        if num3>100:
                            lst.append(num3)
print(' '.join(str(i) for i in lst))
