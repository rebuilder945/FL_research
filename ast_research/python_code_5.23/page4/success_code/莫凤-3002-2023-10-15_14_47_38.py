list1=eval(input())
a=sum(list1)%len(list1)
b=sum(list1)/len(list1)
if a ==0:
    print("%.0f"%(b))
else:
    print("%.2f"%(b))
