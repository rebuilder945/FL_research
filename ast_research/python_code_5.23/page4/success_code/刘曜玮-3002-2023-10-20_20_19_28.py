lst=eval(input())
b=sum(lst)/len(lst)
if type(b)=="int":
    print('%d'%b)
else :
    print("%.2f"%b)
            
