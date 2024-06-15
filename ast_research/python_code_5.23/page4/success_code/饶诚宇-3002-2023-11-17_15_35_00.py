lst=eval(input())
a=sum(lst)
b=a/len(lst)
if type(b)==int:
    print('%.d'%(b))
else:
    print("%.2f"%(b))
