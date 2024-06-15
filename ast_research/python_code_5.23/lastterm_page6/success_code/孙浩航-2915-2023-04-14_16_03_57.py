n=int(input())
k=0
for i in range(100,n+1):
    a = i//100
    b = (i-a*100)//10
    c = (i-a*100-b*10)
    if i == pow(a,3)+pow(b,3)+pow(c,3) and i <1000:
        k=k+1
        if k>0:
            print(i)
if n<152:
    print("none")
    

    
    
    
        

