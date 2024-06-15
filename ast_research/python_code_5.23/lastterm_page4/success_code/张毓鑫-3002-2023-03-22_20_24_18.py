a=eval(input())
b=sum(a)/len(a)
if (sum(a)%len(a)==0):
    print(b)
else:
    print("%.2f" %b)
