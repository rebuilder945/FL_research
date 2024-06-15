ls=eval(input())
a=sum(ls)/len(ls)
if type(a)==float:
    print("%.2f")%(a)
else:
    print(a)
