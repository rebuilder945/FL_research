num=list(input())
ls=[]
for x in num:
    s=(int(x)+5)%10
    ls.append(s)
lt=ls[::-1]
print("".join(str(x) for x in lt))
