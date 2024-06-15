a=list(eval(input()))
b=0
for i in a:
    b=b+i
c=b/len(a)
if type(c)=="class'int'":
    print("%d"%(c))
else:
    print("%.2f"%(c))
