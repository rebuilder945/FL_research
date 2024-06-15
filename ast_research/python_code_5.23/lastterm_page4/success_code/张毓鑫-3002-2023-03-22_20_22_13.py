a=eval(input())
b=sum(a)/len(a)
if type(a)==int:
    print(b)
else:
    print("%,2f" %b)
