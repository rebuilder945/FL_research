a=eval(input())
ls=[]
while a>0:
    b=(a%10+5)%10
    ls.append(b)
    a=a//10
print(*ls,sep="")
