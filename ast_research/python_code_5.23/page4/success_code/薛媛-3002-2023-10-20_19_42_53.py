lst1=eval(input())
if sum(lst1)%len(lst1)==0:
    print("%d"%(sum(lst1)/len(lst1)))
else:
    print("%.2f"%(sum(lst1)/len(lst1)))
