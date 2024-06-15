ls1 = eval(input())
ls2 = []
def sb(x):
    nm = 0
    for i in range(2,x):
        if x%i==0:
            nm+=1
    if x==0 or x==1:
        return 1
    elif nm==0:
        return 0
    else:
        return 1
for x in ls1:
    a = sb(x)
    if a==0:
        ls2.append(x)
print(ls2)
