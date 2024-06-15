ls1=list(str(input().split(',')))
ls2=list (map (int,input().split()))
ls3=[[x,y] for x,y in zip(ls1,ls2)]
print(ls3)
