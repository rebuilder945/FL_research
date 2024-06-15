lst=eval(input())
setlst=list(set(lst))
bst=lst[:]
mot=[]
for x in setlst:
    if bst.count(x)==1:
        mot.append(x)
mot.sort()
newmot=list(map(str,mot))

yaoyao=','.join(newmot)
if len(mot)==0:
    print('False')
else:
    print(yaoyao)
    



        
        
    
    
