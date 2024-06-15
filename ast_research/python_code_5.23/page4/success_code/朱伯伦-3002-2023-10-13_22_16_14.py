list=eval(input())
a=sum(list)/len(list)
if a%1==0:
    print(int(a))
else:
    print("%.2f"%(a))
