list=eval(input())
for x in list:
    x+=x
a=x/len(list)
if x-round(a,2)==0:
    print("%d"%(a))
else:
    print("%.2f"%(a))
