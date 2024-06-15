a=input().split()
b={}
while True:
    for i in range(len(a)):            
        b[a[i]]=b.get(a[i],0)+1    
        c=list(map(int,b.values()))
        for i in range(len(c)):
            if c[i]==max(c):
                print(list(b.keys())[i],c[i]) 

