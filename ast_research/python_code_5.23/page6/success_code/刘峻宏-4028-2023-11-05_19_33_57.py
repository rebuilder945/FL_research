a=eval(input())
b=[]
if a==2:
   b=[2]
elif a<=1 or not a==int(a) :
    print("illegal input")
else:
    b.append(2)
    for i in range(2,a):
        m=0
        for x in range (2,i+1):
        
            if  (i+1)%x==0:
             m=+1
            
        if  m==0:
            b.append(i+1)  

d=[]
e=[]
for i in range (len(b)):
    one=b[i]
    n=0
    while one>0:
        one=one//10
        d.append(one)
    for j in range (len(d)):
        if not d[i]==d[-i-1]:
            n+=1
    if n==0:
        e.append(b[i])
print(e)
    
    
