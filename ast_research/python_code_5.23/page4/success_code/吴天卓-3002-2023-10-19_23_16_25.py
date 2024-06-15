A=eval(input())
a=sum(A)%len(A)
b=sum(A)/len(A)
if a==0:
    print(int(b))
else:
    print("%.2f"%(b))
