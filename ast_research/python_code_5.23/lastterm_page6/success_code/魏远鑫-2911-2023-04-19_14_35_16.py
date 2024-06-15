num=str(eval(input()))
ls=list(num)
for i in range(len(ls)):
    ls[i]=(int(ls[i])+5)%10
ls=ls[::-1]
print(*ls,sep="")

