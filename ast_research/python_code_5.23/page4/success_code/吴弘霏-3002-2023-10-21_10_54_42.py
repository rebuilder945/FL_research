list=eval(input())
a=sum(list)/len(list)
if type(a)==int:
    print(a)
else:
    print("%.2f"%a)

