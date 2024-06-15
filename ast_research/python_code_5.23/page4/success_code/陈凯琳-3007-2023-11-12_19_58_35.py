lit=eval(input())
n,m=eval(input())
if n>m or n>=len(lit):
    print('error')
else:
    lit1=[]
    lit2=[]
    for i in range(n,m):
        lit1.append(lit[i])
    for i in lit:
        if i not in lit1:
            lit2.append(i)
    print(lit2)





        
    










