ls=[]
n,m=map(eval,input().split())
if m-n<3 or m<0 or n<0:
    print("illegal input")
else:
    for x in range(n,m):
        for y in range(n,m):
            for z in range (n,m):
                if x!=y and y!=z and x!=z:
                    a=x*100+y*10+z*1
                    if 99<a<1000:
                     ls.append(a)
if ls==[]:
    print("illegal input")
else:
 ls=str(ls)
 ls=ls.strip('[]')
 ls=ls.replace(",","")
 print(ls)                    
                    
