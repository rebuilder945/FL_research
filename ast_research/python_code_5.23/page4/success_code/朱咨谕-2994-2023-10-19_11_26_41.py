ls1=list(eval(input()))
n,m=eval(input())
if(n<len(ls1)) : 
    for i in range(m) : ls1.append(ls1[n])
else : print('error')
print(ls1)
