a = eval(input())
b = set(a)
save=[]
for i in b:
    
    jishu = a.count(i)
    if jishu==1:
        save.append(i)    
save.sort()
if save==[]:
    print("False")
else:
    save = list(map(str,save))
    print(",".join(save))
        
            
    
    
        
