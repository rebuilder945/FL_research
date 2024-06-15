s=eval(input())
a=sum(s[0:])
b=len(s)
c=a/b
aver=a%b
if aver-b == -b:
    d=a//b
    print(int(d))
elif aver-b < 0:
    print("%.2f"%c)
