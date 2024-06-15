a=list(eval(input()))
b=0
for i in a:
    b=b+i
c=b/len(a)
for i in range(1,int(c)):
    if c%i==0: 
        print(int(c))
        break
else:
    print("%.2f"%(c))
