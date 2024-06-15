lst=eval(input())
a=sum(lst)
b=a/len(lst)
if a%len(lst)==0:
    print(int(b))
else:
    print("%.2f"%(b))
