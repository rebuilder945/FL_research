ls1=eval(input())
e=sum(ls1)/len(ls1)
if e.count('.')==1:
    print("%.2f"%e)
else:
    print(e)
