ls1=input().split(',')
ls2=list(eval(input()))
ls3=list(zip(ls1,ls2))
ls3=sorted(ls3,key=lambda x:x[1])
    
print(ls3)
