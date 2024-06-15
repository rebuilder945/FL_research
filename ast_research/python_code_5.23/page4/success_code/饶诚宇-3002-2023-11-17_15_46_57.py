lst=eval(input())
c=int(lst)
a=sum(c)
b=a/len(c)
if type(b)==int:
    print(int(b))
else:
    print("%.2f"%(b))
