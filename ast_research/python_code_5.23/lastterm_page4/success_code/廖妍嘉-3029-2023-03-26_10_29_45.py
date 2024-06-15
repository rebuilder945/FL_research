ls1=input().split(",")
ls2=list(input()).remove('[]')
for i in range(len(ls1)):
    n=ls1[i]
    m=(ls2[i])
    i = i +1
    ls4=[]
    ls5=[]
    ls4.append(n)
    ls5.append(m)
    print((ls4+ls5),end=',')
    

