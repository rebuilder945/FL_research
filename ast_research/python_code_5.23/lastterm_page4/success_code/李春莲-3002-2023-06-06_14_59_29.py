l=eval(input())
ave=(sum(l)/len(l))
b=int(ave)-ave
if b==0:
    print(int(ave))
else:
    print("%.2f"%(ave))
