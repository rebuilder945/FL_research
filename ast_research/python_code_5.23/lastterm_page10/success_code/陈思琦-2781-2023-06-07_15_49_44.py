number=input()
if len(number)!=18:
    print('Error')
else:
    a=int(number[0])*7
    b=int(number[1])*9    
    c=int(number[2])*10   
    d=int(number[3])*5
    e=int(number[4])*8
    f=int(number[5])*4    
    g=int(number[6])*2   
    h=int(number[7])*1
    i=int(number[8])*6
    j=int(number[9])*3    
    k=int(number[10])*7   
    l=int(number[11])*9
    m=int(number[12])*10
    n=int(number[13])*5    
    o=int(number[14])*8   
    p=int(number[15])*4
    q=int(number[16])*2
    sum=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q
w=int(sum%11)
list=[1,0,'X',9,8,7,6,5,4,3,2]
yu=list[w]
if yu==number[-1]:
    print('Correct')
else:
    print('Wrong')


