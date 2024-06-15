list1=eval(input())
x=sum(list1)/len(list1)
if x%1==0:
    print(int(x))
else:
    print("%.2f"%(x))
