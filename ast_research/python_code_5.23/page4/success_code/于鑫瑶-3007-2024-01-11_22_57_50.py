ls1=eval(input())
n,m=eval(input())
ls2=[]
if m<=len(ls1):
    for x in range(n):
        ls2.append(ls1[x])
    for y in range(m,len(ls1)):
        ls2.append(ls1[y])
    print(ls2)
elif n>=len(ls1):
    print("error")

    
    

