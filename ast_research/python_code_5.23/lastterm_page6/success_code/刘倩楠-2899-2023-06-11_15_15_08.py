n,m=input().split()
a,b=int(n),int(m)
if b-a==3 and 0<=a<=9 and 0<=b<=9:
    w=''
    for x in range(a,b):
        for y in range(a,b):
            for z in range(a,b):
                if x!=y and y!=z and z!=x and x!=0:
                    w+=str(x)+str(y)+str(z)+" "
else:
    print("illegal input") 
    
l=list(w.split())
print(" ".join(l))
