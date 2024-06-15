c=eval(input())
b=sum(c)%len(c)
if b==0:
    print(sum(c)//len(c))
else:
    print("%.2f"%(sum(c)/len(c)))
