n=input() or 'q'
x={}
while n!='q':
    if n not in x:
         x[n]=1
    else:
        x[n]+=1
    print(n,' ',x[n])
    n=input() or 'q'
