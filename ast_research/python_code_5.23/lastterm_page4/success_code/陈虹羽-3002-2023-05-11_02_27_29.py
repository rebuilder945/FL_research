a=eval(input())
b=sum(a)/len(a)
if type(b) is int: 
    print(b)
elif type(b) is float:
    print("%.2f"%(b))

