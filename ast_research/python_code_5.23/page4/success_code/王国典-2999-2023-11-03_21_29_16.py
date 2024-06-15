Is=eval(input())
n,m=eval(input())
Is1=[]
Is1.append(Is[n])
Is[n]=Is[m]
Is[m]=Is1[0]
print(Is)
