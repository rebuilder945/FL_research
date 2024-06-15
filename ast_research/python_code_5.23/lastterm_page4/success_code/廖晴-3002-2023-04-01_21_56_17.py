s=eval(input())
c=sum(s)/len(s)
if c-int(c)==0:
    print("%.d"%c)
else:
    print("%.2f"%c)
