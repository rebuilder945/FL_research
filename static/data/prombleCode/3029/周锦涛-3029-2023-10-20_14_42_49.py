ls1=input().split(',')
ls2=eval(input())
ls3=[]
for x in ls1:
    ls3.append([])
    for y in ls2:
        ls3[int(len(ls3)-1)].append(x+y)
print(ls3)
