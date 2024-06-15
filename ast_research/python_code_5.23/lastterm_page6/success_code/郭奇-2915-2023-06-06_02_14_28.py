n=eval(input())
lst1=[]
if n>100:
    for i in range(n):
        if i[0]**3+i[1]**3+i[2]**3==n:
            lst1.append(i)
        else:
            pass
    else:
        print('none')
        
    
