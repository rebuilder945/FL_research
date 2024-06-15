ls1=eval(input())
for i in ls1:
    e=sum(i)/len(i)
if '.' in e:
    print("%.2f"%e)
else:
    print(e)
