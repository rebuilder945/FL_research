ls1=input().split(',')
ls2=list(eval(input()))
ls3=[[x,y] for x,y in zip(ls1,ls2)]
print(ls3)
