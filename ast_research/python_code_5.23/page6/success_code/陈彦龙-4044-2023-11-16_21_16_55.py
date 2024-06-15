n=input()
a=0
for x in range(100,int(n)+1):
    b=str(x)
    if int(x)==int(b[0])**3+int(b[1])**3+int(b[2])**3:
        print(int(x))
        a+=1
if a==0:
    print('none')        
