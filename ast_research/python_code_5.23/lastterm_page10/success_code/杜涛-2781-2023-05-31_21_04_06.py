b=list(input())
a=list(map(eval,b[:-1]))
if len(b)!=18:
    print('Error')
else:
    s=0
    c=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    for i in range(len(c)):
        s+=a[i]*c[i]
    n=s%11
    lst1=['1','0','X','9','8','7','6','5','4','3','2','1']
    lst2=[x for x in range(0,11)]
    m=(12-n)%11
    q=lst2.index(m)
    if (m==10 and b[-1]=='X') or (m!=10 and lst1[q]==b[-1]):
        print('Correct')
    else:
        print('Wrong')
    
    
        
