x=eval(input())
a1=(x%10+5)%10
a2=(int(x/10)%10+5)%10
a3=(int(x/100)%10+5)%10
print("%d%d%d"%(a1,a2,a3))
