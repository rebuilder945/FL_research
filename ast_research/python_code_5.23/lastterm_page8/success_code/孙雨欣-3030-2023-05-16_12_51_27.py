ls1=input().split(',')
ls2=list(eval(input()))
ls3=[]
for i in range(len(ls1)):
    ls3[i]=[ls1[i],ls2[i]]
    
print(ls3)
