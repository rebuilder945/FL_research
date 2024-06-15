a=eval(input())
b=sum(a)/len(a)
if (sum(a)%len(a)==0):
    print(int(b))
else:
    print("%.2f" %b)
