ls1=input().split(',')
ls2=map(int,input().split(','))
ls3=[]
for i in range(len(ls1)):
    ls3[i]=list(ls1[i],ls2[i])
print(ls3)
