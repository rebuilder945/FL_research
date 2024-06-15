a=eval(input())
b=0
for i in a:
    b=b+i
c=b/len(a)
if a%1==0:
    print(int(c))
else:

    print("%.2f"%(c))


