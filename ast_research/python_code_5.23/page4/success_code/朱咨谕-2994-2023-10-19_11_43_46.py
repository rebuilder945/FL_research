ls1=list(eval(input()))
n,m=eval(input())
print(ls1)
if(n<len(ls1)) : 
    for i in range(m) : ls1.append(ls1[n])
    print(ls1)
else : print('error')
    


        
