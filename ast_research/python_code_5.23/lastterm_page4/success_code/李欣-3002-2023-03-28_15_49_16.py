ls1=eval(input())
e=sum(ls1)/len(ls1)
if '.' in e:
    print("%.2f"%e)
else:
    print(e)
