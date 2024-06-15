ls1=list(str(input().split(',')))
ls2=int(input().split("."))
ls3=[x for x,y in zip(ls1,ls2)]
print(ls3)
