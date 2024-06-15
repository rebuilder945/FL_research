list1=eval(input())
h=sum(list1)/len(list1)
if h%1!=0:
    print("%.2f"%(h)) 
else:
    print(h)
