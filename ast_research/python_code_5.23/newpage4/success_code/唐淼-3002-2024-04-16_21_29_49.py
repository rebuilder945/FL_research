lst=eval(input())
a=sum(lst[::])
b=a/len(lst)
if type(b)==int:
    print(b)
if type(b)==float:
    print("%.2f"%(b))
