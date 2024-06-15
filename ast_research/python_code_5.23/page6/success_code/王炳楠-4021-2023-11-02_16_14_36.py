n=eval(input())
if n>=3:
    ls1=[2,3]
    ls2=[1,2]
    for i in range(n-2):
        ls1.append(ls1[-1]+ls1[-2])
        ls2.append(ls2[-1]+ls2[-2])
    su=0
    for x in range(n):
        su=su+ls1[x]/ls2[x]
    print("%.4f"%(su))
elif n==1:
    print("%.4f"%(2/1))
elif n==2:
    print("%.4f"%(2+1.5))

        

