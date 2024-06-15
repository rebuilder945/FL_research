
lst=eval(input())
b=sum(lst)/len(lst)
if type(b)=="<class 'float'>":
    print('%d'%b)
else :
    print("%.2f"%b)
            
