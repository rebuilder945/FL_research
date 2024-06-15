a=eval(input())
sum(a)
average=sum(a)/len(a)
if sum(a)%len(a)==0:
    print(int(average))
else:
    print("%.2f"%average)
