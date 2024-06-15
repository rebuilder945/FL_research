lst=eval(input())
result=sum(lst)/len(lst)
if result-int(result)==0 :
    print(int(result))
else :
    print("%.2f"%(result))    
