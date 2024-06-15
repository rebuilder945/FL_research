lst=eval(int,input())
a=sum(lst)
b=a/len(lst)
if type(b)==int:
    print(int(b))
else:
    print("%.2f"%(b))
