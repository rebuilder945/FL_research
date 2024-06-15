n,m=map(int,input().split())
if m-n<3:
    print("illegal input")
else:    
    l=[]
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                k=x*100+y*10+z
                if k<100 or x==y or x==z or z==y:
                     continue
                else:
                     l.append(k)
    for m in l:
            print(m,end=' ')
            


            
    



