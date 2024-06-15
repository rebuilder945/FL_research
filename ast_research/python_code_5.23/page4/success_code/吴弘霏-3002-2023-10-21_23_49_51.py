list=eval(input())
a=str(sum(list)/len(list))
if type(a)==int:
    print(a)
elif type(a)==float:
    print("%.2f"%a)

