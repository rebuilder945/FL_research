lst=eval(input())
newlist=[]
for i in lst :
    for m in range(2,i) :
        if type(i // m)==int :
            break
        else:    
            newlist.append(i)
print(newlist)            
