num=eval(input())
s=sum(num)
d=len(num)
if s/d==s//d:
    print(s//d)
else:
    print("%.2f" %(s/d))

