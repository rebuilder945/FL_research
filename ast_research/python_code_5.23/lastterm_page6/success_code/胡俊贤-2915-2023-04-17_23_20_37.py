n=int(input())
m=0
if len(str(n))==3:
    for i in range(100,n+1):
        s=str(i)
        a=int(s[0])**3+int(s[1])**3+int(s[2])**3
        if i==a:
            print(i)
            m+=1
if m ==0:
    print('none')

    
