n=eval(input())
if type(n)==float or n<0:
    print("illegal input")
else:
    t=[]
    for x in range(2,n+1):
        for i in range(2,x):
            if x%i==0:
                break
        else:
                if  str(x)==str(x)[::-1] and x not in t:
                    t.append(x)  
for i in range (len(t))  :                    
    print('%d'%t[i],end=' ') 

