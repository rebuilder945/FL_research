list1=eval(input())
x=sum(list1)/len(list1)
if type(x)==int:
    print(int(x))
elif type(x)==float:
    print("%.2f"%(x))
